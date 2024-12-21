import os  # Importing the os module to perform file-related operations.
import winsound  # Importing winsound to play sounds for Morse code (Windows-specific feature).

# Step 1: Creating a dictionary to map letters, numbers, and symbols to their Morse code representations.
# Each key in the dictionary is a character (like 'A', '1', ',') and its corresponding value is the Morse code.
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

# Step 2: Creating a reverse dictionary for converting Morse code back to text.
# This takes the original MORSE_CODE_DICT and swaps the keys and values.
# Now, we can use Morse code as the key and get the corresponding character as the value.
# For example, '.-' (Morse code for 'A') will now map back to 'A'.
TEXT_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


# Function to convert text into Morse code.
def text_to_morse(text):
    """
    Converts a given text into its Morse code representation.

    :param text: Input string to convert into Morse code.
    :return: A string containing the Morse code representation of the input text.
    """
    morse_code = []  # Initialize an empty list to store the Morse code.

    # Loop through each character in the input text (converted to uppercase).
    for char in text.upper():
        # Check if the character exists in the Morse code dictionary.
        if char in MORSE_CODE_DICT:
            # If it exists, append the corresponding Morse code to the list.
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            # If it doesn't exist, append a '?' to indicate an unsupported character.
            morse_code.append("?")

    # Join the list of Morse code with spaces and return it as a single string.
    return ' '.join(morse_code)


# Function to convert Morse code back into text.
def morse_to_text(morse_code):
    """
    Converts a given Morse code back into its text representation.

    :param morse_code: Input Morse code string to convert into text.
    :return: A string containing the text representation of the Morse code.
    """
    text = []  # Initialize an empty list to store the decoded text.

    # Split the Morse code string by spaces to get individual Morse code symbols.
    for code in morse_code.split():
        # Check if the Morse code exists in the reverse dictionary.
        if code in TEXT_DICT:
            # If it exists, append the corresponding character to the list.
            text.append(TEXT_DICT[code])
        else:
            # If it doesn't exist, append a '?' to indicate an unsupported Morse code.
            text.append("?")

    # Join the list of characters into a single string and return it.
    return ''.join(text)


# Function to play Morse code as sound.
def play_morse(morse_code):
    """
    Plays the given Morse code as sound using the winsound module.
    Dots are short beeps, dashes are long beeps, and spaces are pauses.

    :param morse_code: Input Morse code string to play as sound.
    """
    for symbol in morse_code:
        if symbol == '.':
            # Play a short beep for a dot.
            winsound.Beep(1000, 200)  # Frequency: 1000 Hz, Duration: 200 ms
        elif symbol == '-':
            # Play a long beep for a dash.
            winsound.Beep(1000, 600)  # Frequency: 1000 Hz, Duration: 600 ms
        elif symbol == ' ':
            # Pause briefly between letters.
            winsound.Beep(37, 300)  # A very low frequency sound to act as a pause.
        elif symbol == '/':
            # Pause longer between words.
            winsound.Beep(37, 600)  # A very low frequency sound to act as a pause.


# Function to save Morse code to a file.
def save_to_file(filename, content):
    """
    Saves the given content (text or Morse code) to a file.

    :param filename: Name of the file to save the content to.
    :param content: The content to save (text or Morse code).
    """
    with open(filename, 'w') as file:
        file.write(content)  # Write the content to the file.
    print(f"Saved to {filename}.")  # Confirm that the content was saved.


# Function to load Morse code from a file.
def load_from_file(filename):
    """
    Loads the content of a file and returns it as a string.

    :param filename: Name of the file to load the content from.
    :return: The content of the file as a string, or None if the file doesn't exist.
    """
    if os.path.exists(filename):  # Check if the file exists.
        with open(filename, 'r') as file:
            return file.read().strip()  # Read the file and return the content.
    else:
        print(f"{filename} not found.")  # Print an error message if the file doesn't exist.
        return None


# Main menu to interact with the user.
def main():
    """
    Provides a menu-based interface for the Morse code converter.
    """
    print("Morse Code Converter")  # Print the title of the program.
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")
    print("3. Play Morse Code as Sound")
    print("4. Save Morse Code to File")
    print("5. Load Morse Code from File")
    print("6. Exit")

    # Start a loop to continuously show the menu and get user input.
    while True:
        choice = input("\nEnter your choice: ")  # Prompt the user for a choice.

        if choice == '1':  # If the user chooses option 1:
            text = input("Enter the text: ")  # Get the text input from the user.
            morse_code = text_to_morse(text)  # Convert the text to Morse code.
            print(f"Morse Code: {morse_code}")  # Print the Morse code.
        elif choice == '2':  # If the user chooses option 2:
            morse_code = input("Enter the Morse code (use spaces between letters): ")
            text = morse_to_text(morse_code)  # Convert the Morse code to text.
            print(f"Text: {text}")  # Print the decoded text.
        elif choice == '3':  # If the user chooses option 3:
            morse_code = input("Enter the Morse code to play: ")
            play_morse(morse_code)  # Play the Morse code as sound.
        elif choice == '4':  # If the user chooses option 4:
            text = input("Enter the text to save as Morse code: ")
            morse_code = text_to_morse(text)  # Convert the text to Morse code.
            filename = input("Enter the filename to save: ")
            save_to_file(filename, morse_code)  # Save the Morse code to a file.
        elif choice == '5':  # If the user chooses option 5:
            filename = input("Enter the filename to load: ")
            morse_code = load_from_file(filename)  # Load Morse code from the file.
            if morse_code:
                print(f"Loaded Morse Code: {morse_code}")
                text = morse_to_text(morse_code)  # Convert the Morse code to text.
                print(f"Text: {text}")
        elif choice == '6':  # If the user chooses option 6:
            print("Exiting...")  # Exit the program.
            break  # Break the loop to end the program.
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input.


# Run the main menu if this file is executed directly.
if __name__ == "__main__":
    main()
