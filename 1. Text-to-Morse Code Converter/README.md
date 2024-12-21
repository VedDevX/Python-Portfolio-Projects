# Morse Code Converter

A simple Python-based program that allows you to convert text into Morse code and vice versa. This project includes the ability to play Morse code as sound, save Morse code to a file, and load it from a file. It demonstrates fundamental concepts like string manipulation, file handling, and sound processing in Python.

---

## Features

- **Text to Morse Code Conversion**: Converts a given text message into its corresponding Morse code.
- **Morse Code to Text Conversion**: Decodes a Morse code sequence back into the original text.
- **Morse Code Sound**: Plays Morse code using sound, where dots are short beeps and dashes are long beeps.
- **Save Morse Code to File**: Allows saving the converted Morse code into a text file for later use.
- **Load Morse Code from File**: Loads Morse code from a file and decodes it back to text.

---

## Requirements

- Python 3.x
- **Windows OS** (for sound playback using `winsound` module)

---

## Installation

1. Clone this repository to your local machine.

```bash
git clone https://github.com/VedDevX/Python-Portfolio-Projects/1. Text-to-Morse-Code-Converter.git
```

# How to Use
1. Run the Program:
   Run the Python script to launch the program.
   ```bash
   python main.py
   ```

## Menu Options

You will be presented with a menu to choose the desired operation:

1. **Convert Text to Morse Code**: Enter text to convert it into Morse code.
2. **Convert Morse Code to Text**: Enter Morse code to decode it back to text.
3. **Play Morse Code as Sound**: Enter Morse code to hear it as sound.
4. **Save Morse Code to File**: Save the converted Morse code to a file.
5. **Load Morse Code from File**: Load Morse code from a file and decode it.
6. **Exit**: Exit the program.

## Input Format

- For **Text to Morse Code**, type the text message (e.g., `Hello World`).
- For **Morse Code to Text**, type the Morse code using spaces between characters (e.g., `.... . .-.. .-.. --- / .-- --- .-. .-.. -..`).
- For **Sound Playback**, type the Morse code to hear it.
- For **Save/Load**, provide the filename for saving/loading Morse code.

## Example

### Text to Morse Code:
- **Input**: `Hello`
- **Output**: `.... . .-.. .-.. ---`

### Morse Code to Text:
- **Input**: `.... . .-.. .-.. ---`
- **Output**: `Hello`

### Play Morse Code as Sound:
- **Input**: `.... . .-.. .-.. ---`
  (You will hear short and long beeps corresponding to the Morse code)


## Code Explanation

- **MORSE_CODE_DICT**: A dictionary mapping each letter, number, and symbol to its Morse code representation.
- **TEXT_DICT**: A reverse dictionary to convert Morse code back into text.
- **text_to_morse()**: Converts text input into Morse code.
- **morse_to_text()**: Converts Morse code back into text.
- **play_morse()**: Plays the Morse code as sound using the `winsound` module.
- **save_to_file()**: Saves the Morse code to a file.
- **load_from_file()**: Loads Morse code from a file.

## Contributing

If you have any suggestions or improvements, feel free to fork this repository and create a pull request. Contributions are always welcome!

## Acknowledgments

Thanks to the Python community for providing great libraries and resources.  
Special thanks to the Morse code pioneers for creating this encoding system.

## Contact

Feel free to reach out to me at [vedant.jadhav1928@gmail.com] for any questions or comments.

