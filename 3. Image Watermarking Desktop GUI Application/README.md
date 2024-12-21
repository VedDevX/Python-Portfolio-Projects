# Image Watermarking Tool

## Overview
The **Image Watermarking Tool** is a desktop application developed in Python using the `Tkinter` library for the graphical user interface (GUI) and `Pillow` for image processing. The tool allows users to add custom text watermarks to images with complete control over the watermark's appearance, including the font, font size, color, and position. This easy-to-use application supports various image formats such as PNG, JPEG, and BMP. It is ideal for anyone who wants to quickly add a watermark to an image before sharing or publishing it.

## Features
- **Add Custom Watermark:** Insert custom text as a watermark on any image.
- **Font Selection:** Choose a font for the watermark text from system-installed fonts.
- **Adjust Font Size:** Change the size of the watermark text using a slider.
- **Color Picker:** Pick the color for the watermark text from a color picker dialog.
- **Position Control:** Select the position of the watermark (top-left, top-right, bottom-left, bottom-right).
- **Image Preview:** Preview the image with the watermark before saving.
- **Save Watermarked Image:** Save the final image with the watermark applied in PNG or JPEG formats.

## Installation

### Requirements
- Python 3.x
- Tkinter (for GUI)
- Pillow (for image processing)
- `colorchooser` (for color selection)

### Installing Dependencies
To get started, make sure you have Python 3.x installed. Then, install the required dependencies using `pip` by running the following commands:

```bash
pip install tk
pip install pillow
```

## How to Use

1. **Open an Image**  
   Click the **"Open Image"** button to open a file dialog and select an image from your computer. The image will be loaded into the application.

2. **Enter Watermark Text**  
   In the **"Enter Watermark Text:"** input field, type the text you want to use as a watermark on the image.

3. **Customize Watermark**  
   - **Select Font:** Click on the **"Select Font"** button to choose a font file (TTF or OTF) from your system.
   - **Adjust Font Size:** Use the **"Font Size"** slider to adjust the size of the watermark text.
   - **Pick Text Color:** Click on the **"Select Text Color"** button to choose a color for the watermark text from a color picker.
   - **Position:** Use the **"Choose Watermark Position"** dropdown to select where you want the watermark to appear on the image (top-left, top-right, bottom-left, bottom-right).

4. **Save Watermarked Image**  
   Once you're satisfied with the watermark settings, click the **"Save Watermarked Image"** button. You’ll be prompted to choose the file format (PNG or JPEG) and specify a location to save the image with the watermark applied.


## Application Flow

1. **Launch Application**
   - The application is launched, and the main window is displayed with the options to open an image, add watermark text, and customize watermark settings.

2. **Open Image**
   - The user clicks the **"Open Image"** button, which triggers a file dialog.
   - The user selects an image from their system.
   - The image is loaded and displayed in the application window.

3. **Watermark Customization**
   - The user enters the watermark text in the provided input field.
   - The user selects a font by clicking the **"Select Font"** button, which opens a file dialog to choose a font file.
   - The user adjusts the font size using the **"Font Size"** slider.
   - The user chooses a color for the watermark text using the **"Select Text Color"** button, which opens a color picker.
   - The user selects the position of the watermark (top-left, top-right, bottom-left, bottom-right).

4. **Apply Watermark**
   - Once the user customizes the watermark settings, the watermark is applied to the image.
   - The image is processed with the watermark text, size, color, and position specified by the user.

5. **Save Watermarked Image**
   - The user clicks the **"Save Watermarked Image"** button to save the watermarked image.
   - A file dialog appears, prompting the user to choose the file name, file format (PNG or JPEG), and save location.
   - The watermarked image is saved to the specified location.

## Code Explanation

### Core Functions

#### `open_image()`
This function opens a file dialog to allow the user to select an image file. Once an image is selected, it is displayed in the application window.

#### `load_image(image_path)`
This function takes the path of the selected image and loads it into the application as a thumbnail for preview. It resizes the image to fit into the application window.

#### `add_watermark(image_path, watermark_text, position, font_size, font_color)`
This is the core function that adds the watermark to the image. It opens the image, uses the `ImageDraw.Draw()` method to add the text watermark, and applies the font settings such as size and color. The watermark can be positioned at one of four corners based on the user’s selection.

#### `save_image()`
This function allows the user to save the image with the watermark. The user is prompted to specify the save location and file format (PNG or JPEG). If no image is loaded or if no watermark text is entered, an error message is shown.

#### `select_font()`
Opens a file dialog to allow the user to select a font file (either TTF or OTF). The selected font is then used for the watermark text.

#### `choose_color()`
Opens the color chooser dialog and allows the user to pick a color for the watermark text. The selected color is displayed in a preview box.

---

## GUI Layout

### Tkinter Canvas and Scrollbars
The main interface is built using Tkinter. The application has a canvas with a vertical scrollbar to handle all widgets, including buttons, sliders, and labels.

### Buttons and Sliders
Buttons are used for opening an image, selecting a font, choosing a color, and saving the image. A slider allows the user to adjust the watermark font size.
