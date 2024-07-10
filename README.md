
# License Plate Detection and Recognition

This project detects and recognizes license plates from an image using OpenCV and Tesseract OCR.

## Requirements

- Python 3.x
- OpenCV
- imutils
- pytesseract
- tkinter

## Installation

1. Install Python 3.x from the [official website](https://www.python.org/).
2. Install the required Python packages using pip:

```bash
pip install numpy opencv-python imutils pytesseract
```

3. Install Tesseract OCR:
   - **Windows:** Download the Tesseract installer from [here](https://github.com/UB-Mannheim/tesseract/wiki) and follow the installation instructions.
   - **Linux:** Install Tesseract using your package manager. For example, on Ubuntu:

```bash
sudo apt-get install tesseract-ocr
```

## Usage

1. Run the script:

```bash
python license_plate_recognition.py
```

2. A file dialog will appear. Select the image file you want to process.
3. The script will display the original image, the edges detected, and the detected license plate (if found). It will also print the recognized text from the license plate.

## Code Explanation

The code performs the following steps:

1. Initializes Tkinter and opens a file dialog to select an image file.
2. Reads the selected image file and resizes it.
3. Converts the image to grayscale and applies a bilateral filter to reduce noise while keeping edges sharp.
4. Detects edges in the image using Canny edge detection.
5. Finds contours in the edged image and sorts them based on area to find potential license plates.
6. Looks for contours that resemble a license plate (i.e., a contour with four points).
7. Creates a mask for the detected license plate and extracts it.
8. Converts the extracted license plate to grayscale and applies a threshold to prepare it for OCR.
9. Uses Tesseract OCR to extract text from the processed image and prints the recognized text.

## Example Output

After running the script and selecting an image, you will see the following windows:

- **Original Image:** Displays the selected image.
- **Edged:** Displays the edges detected in the image.
- **Number Plate:** Displays the detected license plate (if found).
- **Processed Number Plate:** Displays the thresholded license plate ready for OCR.

The recognized text from the license plate will be printed in the console.

## Notes

- Make sure Tesseract OCR is properly installed and its path is added to the system's PATH environment variable.
- The accuracy of license plate detection and recognition depends on the quality of the input image.

