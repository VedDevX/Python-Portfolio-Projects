import tkinter as tk
from tkinter import messagebox, ttk
import time
import requests
import json
import os


class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("800x600")
        self.leaderboard_file = "leaderboard.json"
        self.selected_paragraph = ""
        self.start_time = None
        self.username = ""

        # Black and Yellow Theme
        self.bg_color = "#000000"  # Black background
        self.text_color = "#FFD700"  # Yellow text
        self.button_bg = "#000000"  # Black button
        self.button_fg = "#FFD700"  # Yellow button text
        self.button_hover = "#FFD700"  # Yellow button hover effect
        self.text_area_bg = "#000000"  # Black text area
        self.text_area_fg = "#FFD700"  # Yellow text in text area

        self.create_widgets()
        self.fetch_paragraph()
        self.load_leaderboard()

    def create_widgets(self):
        # Create Canvas for the entire UI
        self.canvas = tk.Canvas(self.root, bg=self.bg_color)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Create Scrollbar for the Canvas
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create a frame inside the canvas
        self.main_frame = tk.Frame(self.canvas, bg=self.bg_color)
        self.canvas.create_window((0, 0), window=self.main_frame, anchor="nw")

        self.main_frame.bind(
            "<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Title
        title_label = tk.Label(self.main_frame, text="Typing Speed Test", font=("Helvetica", 24, "bold"), bg=self.bg_color, fg=self.text_color)
        title_label.pack(pady=20)

        # Username Input
        username_label = tk.Label(self.main_frame, text="Enter your name:", font=("Helvetica", 14), bg=self.bg_color, fg=self.text_color)
        username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.main_frame, font=("Helvetica", 14), bg=self.text_area_bg, fg=self.text_area_fg, insertbackground=self.text_area_fg)
        self.username_entry.pack(pady=10)

        # Difficulty Dropdown
        difficulty_label = tk.Label(self.main_frame, text="Select Difficulty:", font=("Helvetica", 14), bg=self.bg_color, fg=self.text_color)
        difficulty_label.pack(pady=5)
        self.difficulty = ttk.Combobox(self.main_frame, values=["Easy", "Medium", "Hard"], state="readonly", font=("Helvetica", 12))
        self.difficulty.current(0)
        self.difficulty.pack(pady=10)
        self.difficulty.bind("<<ComboboxSelected>>", lambda e: self.fetch_paragraph())

        # Paragraph Display
        self.paragraph_display = tk.Label(self.main_frame, text="", wraplength=750, font=("Helvetica", 14), justify="left", bg=self.bg_color, fg=self.text_color)
        self.paragraph_display.pack(padx=20, pady=10)

        # Text Area
        self.typing_area = tk.Text(self.main_frame, height=10, wrap="word", font=("Helvetica", 14), bg=self.text_area_bg, fg=self.text_area_fg, bd=0, padx=10, pady=10, insertbackground=self.text_area_fg)
        self.typing_area.pack(padx=20, pady=10)
        self.typing_area.bind("<FocusIn>", self.start_timer)
        self.typing_area.bind("<KeyRelease>", self.update_live_wpm)

        # Live WPM Display
        self.live_wpm_label = tk.Label(self.main_frame, text="Live WPM: 0.00", font=("Helvetica", 14), bg=self.bg_color, fg=self.text_color)
        self.live_wpm_label.pack(pady=5)

        # Submit Button
        submit_button = tk.Button(self.main_frame, text="Submit", command=self.calculate_speed, font=("Helvetica", 14), bg=self.button_bg, fg=self.button_fg, activebackground=self.button_hover)
        submit_button.pack(pady=10, ipadx=20, ipady=10)

        # Reset Button
        reset_button = tk.Button(self.main_frame, text="Reset", command=self.reset_test, font=("Helvetica", 14), bg=self.button_bg, fg=self.button_fg, activebackground=self.button_hover)
        reset_button.pack(pady=5, ipadx=20, ipady=10)

        # Leaderboard Button
        leaderboard_button = tk.Button(self.main_frame, text="View Leaderboard", command=self.show_leaderboard, font=("Helvetica", 14), bg=self.button_bg, fg=self.button_fg, activebackground=self.button_hover)
        leaderboard_button.pack(pady=10, ipadx=20, ipady=10)

    def fetch_paragraph(self):
        """Fetch a meaningful paragraph using the ZenQuotes API."""
        try:
            response = requests.get("https://zenquotes.io/api/quotes", timeout=10)
            response.raise_for_status()
            data = response.json()

            quotes = [quote['q'] for quote in data[:5]]
            self.selected_paragraph = " ".join(quotes)
            self.paragraph_display.config(text=self.selected_paragraph)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching paragraph: {e}")
            self.use_fallback_paragraph()

    def use_fallback_paragraph(self):
        """Use a fallback paragraph if the API call fails."""
        self.selected_paragraph = (
            "Success is not the key to happiness. Happiness is the key to success. "
            "If you love what you are doing, you will be successful."
        )
        self.paragraph_display.config(text=self.selected_paragraph)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def update_live_wpm(self, event):
        """Update the live WPM as the user types."""
        if self.start_time is None:
            return

        current_time = time.time()
        time_elapsed = current_time - self.start_time
        typed_text = self.typing_area.get("1.0", "end-1c").strip()

        if typed_text:
            word_count = len(typed_text.split())
            live_wpm = (word_count / time_elapsed) * 60
            self.live_wpm_label.config(text=f"Live WPM: {live_wpm:.2f}")
        else:
            self.live_wpm_label.config(text="Live WPM: 0.00")

    def calculate_speed(self):
        if self.start_time is None:
            messagebox.showerror("Error", "Start typing to begin the test!")
            return

        end_time = time.time()
        typed_text = self.typing_area.get("1.0", "end-1c").strip()

        if not typed_text:
            messagebox.showerror("Error", "You haven't typed anything!")
            return

        if not self.username_entry.get():
            messagebox.showerror("Error", "Please enter your name!")
            return

        time_taken = end_time - self.start_time
        word_count = len(typed_text.split())
        wpm = (word_count / time_taken) * 60

        original_words = self.selected_paragraph.split()
        typed_words = typed_text.split()
        correct_words = sum(1 for o, t in zip(original_words, typed_words) if o == t)
        accuracy = (correct_words / len(original_words)) * 100

        result_message = (
            f"Time Taken: {time_taken:.2f} seconds\n"
            f"Words Per Minute: {wpm:.2f} WPM\n"
            f"Accuracy: {accuracy:.2f}%"
        )
        messagebox.showinfo("Typing Speed Test Result", result_message)

        self.save_to_leaderboard(self.username_entry.get(), wpm, accuracy)

    def save_to_leaderboard(self, username, wpm, accuracy):
        entry = {"name": username, "wpm": wpm, "accuracy": accuracy}
        self.leaderboard.append(entry)
        self.leaderboard.sort(key=lambda x: x["wpm"], reverse=True)

        with open(self.leaderboard_file, "w") as f:
            json.dump(self.leaderboard, f)

    def reset_test(self):
        self.typing_area.delete("1.0", "end")
        self.start_time = None
        self.live_wpm_label.config(text="Live WPM: 0.00")

    def load_leaderboard(self):
        if os.path.exists(self.leaderboard_file):
            with open(self.leaderboard_file, "r") as f:
                self.leaderboard = json.load(f)
        else:
            self.leaderboard = []

    def show_leaderboard(self):
        leaderboard_window = tk.Toplevel(self.root)
        leaderboard_window.title("Leaderboard")
        leaderboard_window.geometry("400x300")
        leaderboard_window.configure(bg=self.bg_color)

        leaderboard_label = tk.Label(leaderboard_window, text="Leaderboard", font=("Helvetica", 16), bg=self.bg_color, fg=self.text_color)
        leaderboard_label.pack(pady=10)

        if not self.leaderboard:
            no_data_label = tk.Label(leaderboard_window, text="No data available.", bg=self.bg_color, fg=self.text_color)
            no_data_label.pack(pady=10)
            return

        leaderboard_table = ttk.Treeview(leaderboard_window, columns=("Name", "WPM", "Accuracy"), show="headings", height=10)
        leaderboard_table.column("Name", width=120)
        leaderboard_table.column("WPM", width=80)
        leaderboard_table.column("Accuracy", width=100)
        leaderboard_table.heading("Name", text="Name")
        leaderboard_table.heading("WPM", text="WPM")
        leaderboard_table.heading("Accuracy", text="Accuracy (%)")

        for entry in self.leaderboard:
            leaderboard_table.insert("", "end", values=(entry["name"], f"{entry['wpm']:.2f}", f"{entry['accuracy']:.2f}"))

        leaderboard_table.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
