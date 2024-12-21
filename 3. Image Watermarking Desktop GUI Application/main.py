# Import necessary libraries for GUI and image processing
import tkinter as tk  # Tkinter for GUI
from tkinter import filedialog, messagebox, colorchooser  # For file dialog, messages, and color picking
from PIL import Image, ImageDraw, ImageFont, ImageTk  # Pillow for image manipulation


# Function to add watermark to the image
def add_watermark(image_path, watermark_text, position, font_size, font_color):
    """
    This function adds a watermark (text) to an image at the specified position with chosen font size and color.
    """
    # Open the image from the provided file path
    original_image = Image.open(image_path)
    width, height = original_image.size  # Get the image width and height

    # Create a drawing context to modify the image
    drawing = ImageDraw.Draw(original_image)

    # Load the font for the watermark (default font used if there's an issue)
    try:
        font = ImageFont.truetype(selected_font, font_size)
    except IOError:
        font = ImageFont.load_default()  # Use the default font if the custom font fails

    # Calculate the size of the watermark text to position it properly
    bbox = drawing.textbbox((0, 0), watermark_text, font=font)  # Get bounding box of text
    text_width = bbox[2] - bbox[0]  # Width of the text
    text_height = bbox[3] - bbox[1]  # Height of the text

    # Set the position for the watermark based on user selection
    if position == "top-left":
        position = (10, 10)  # 10px from the top-left corner
    elif position == "top-right":
        position = (width - text_width - 10, 10)  # 10px from the top-right corner
    elif position == "bottom-left":
        position = (10, height - text_height - 10)  # 10px from the bottom-left corner
    elif position == "bottom-right":
        position = (width - text_width - 10, height - text_height - 10)  # 10px from the bottom-right corner

    # Apply the watermark text onto the image at the calculated position
    drawing.text(position, watermark_text, font=font, fill=font_color)

    return original_image  # Return the image with the watermark added


# Function to open and load an image
def open_image():
    """
    Opens a file dialog to allow the user to select an image file.
    """
    global original_image_path  # Use a global variable to store the image path
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])  # Filter for image types
    if file_path:  # If a file is selected
        original_image_path = file_path  # Store the image path globally
        load_image(file_path)  # Load and display the image in the GUI


# Function to load and display the image in the GUI
def load_image(image_path):
    """
    Loads the selected image and resizes it to fit the GUI preview area.
    """
    global panel  # Reference to the image display panel
    image = Image.open(image_path)  # Open the image file
    image.thumbnail((400, 400))  # Resize the image to fit the GUI (400x400 max size)
    img_display = ImageTk.PhotoImage(image)  # Convert the image to a format that can be displayed in Tkinter

    # Display the image in the panel
    panel.config(image=img_display)
    panel.image = img_display  # Keep a reference to the image object


# Function to save the image with the watermark
def save_image():
    """
    Saves the watermarked image to a user-specified location.
    """
    if not original_image_path:  # Check if an image is loaded
        messagebox.showerror("Error", "No image loaded.")  # Show error if no image is loaded
        return

    watermark_text = watermark_entry.get()  # Get the watermark text from the input field
    if not watermark_text:  # Check if the watermark text is empty
        messagebox.showerror("Error", "Please enter watermark text.")  # Show error if text is empty
        return

    position = position_var.get()  # Get the watermark position from the dropdown
    font_size = size_slider.get()  # Get the font size from the slider
    font_color = color_var.get()  # Get the selected font color

    # Add the watermark to the image using the selected options
    watermarked_image = add_watermark(original_image_path, watermark_text, position, font_size, font_color)

    # Ask the user where to save the image
    file_types = [("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")]  # Supported file types
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=file_types)  # File save dialog
    if save_path:  # If a save path is selected
        try:
            watermarked_image.save(save_path)  # Save the image with the watermark
            messagebox.showinfo("Success", f"Watermarked image saved as {save_path}")  # Success message
        except Exception as e:
            messagebox.showerror("Error", f"Unable to save image: {str(e)}")  # Error message if save fails


# Function to select the font for the watermark text
def select_font():
    """
    Opens a file dialog for the user to select a custom font file.
    """
    global selected_font  # Use a global variable for the font selection
    file_path = filedialog.askopenfilename(filetypes=[("Font Files", "*.ttf *.otf")])  # Font file types
    if file_path:  # If a font is selected
        selected_font = file_path  # Store the font file path globally


# Function to open the color chooser and update the color preview
def choose_color():
    """
    Opens a color chooser dialog for the user to pick a color for the watermark text.
    """
    color_code = colorchooser.askcolor()[1]  # Get the color code from the color chooser
    if color_code:  # If a color is selected
        color_var.set(color_code)  # Update the color variable
        color_preview.config(bg=color_code)  # Update the color preview label


# GUI setup using Tkinter
root = tk.Tk()  # Create the main application window
root.title("Image Watermarking Tool")  # Set the window title

# Global variables to store the state
original_image_path = None  # Variable to store the image path
selected_font = "arial.ttf"  # Default font path (Arial)

# Create a frame for the content within the main window
frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Add a canvas to the frame with a vertical scrollbar for scrolling content
canvas = tk.Canvas(frame)
scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)  # Create a scrollbar
canvas.configure(yscrollcommand=scrollbar.set)  # Configure the canvas to use the scrollbar

# Create a second frame inside the canvas to hold all the widgets (buttons, text fields, etc.)
inner_frame = tk.Frame(canvas)

# Add the inner frame to the canvas window (to make it scrollable)
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

# Configure the scrollbar to work with the canvas
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Add a button for opening an image file
open_button = tk.Button(inner_frame, text="Open Image", command=open_image)
open_button.pack(pady=5)

# Add a button for selecting the font
font_button = tk.Button(inner_frame, text="Select Font", command=select_font)
font_button.pack(pady=5)

# Add a label and text field for entering the watermark text
watermark_label = tk.Label(inner_frame, text="Enter Watermark Text:")
watermark_label.pack()

watermark_entry = tk.Entry(inner_frame, width=40)
watermark_entry.pack(pady=5)

# Add a button for selecting the text color
color_button = tk.Button(inner_frame, text="Select Text Color", command=choose_color)
color_button.pack(pady=5)

# Add a label to preview the selected color
color_var = tk.StringVar(value="#FFFFFF")  # Default color is white
color_preview = tk.Label(inner_frame, text="Color Preview", bg=color_var.get(), width=20)
color_preview.pack(pady=5)

# Add a slider for selecting the font size
size_label = tk.Label(inner_frame, text="Font Size:")
size_label.pack(pady=5)

size_slider = tk.Scale(inner_frame, from_=10, to=100, orient="horizontal", length=200, label="Font Size")
size_slider.set(30)  # Default font size is 30
size_slider.pack(pady=5)

# Add a dropdown for selecting the watermark position
position_var = tk.StringVar(value="bottom-right")  # Default position is bottom-right
position_label = tk.Label(inner_frame, text="Choose Watermark Position:")
position_label.pack(pady=5)

position_menu = tk.OptionMenu(inner_frame, position_var, "top-left", "top-right", "bottom-left", "bottom-right")
position_menu.pack(pady=5)

# Add a button to save the image with the watermark
save_button = tk.Button(inner_frame, text="Save Watermarked Image", command=save_image)
save_button.pack(pady=10)

# Create a label to display the selected image
panel = tk.Label(inner_frame)
panel.pack(padx=10, pady=10)


# Function to update the scroll region of the canvas when the inner frame changes
def update_scroll_region(event):
    canvas.config(scrollregion=canvas.bbox("all"))  # Update the scrollable area to match the inner frame


# Bind the event to update the scroll region when the content size changes
inner_frame.bind("<Configure>", update_scroll_region)

# Run the Tkinter application
root.mainloop()
