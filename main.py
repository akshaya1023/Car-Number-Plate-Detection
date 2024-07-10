import numpy as np
import cv2
import imutils
import pytesseract
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Initialize Tkinter and hide the root window
Tk().withdraw()

# Open a file dialog to select an image file
filename = askopenfilename()
if filename:
    image = cv2.imread(filename)  # Use the selected file path

    # Resize the image
    image = imutils.resize(image, width=500)
    cv2.imshow("Original Image", image)

    # Convert to grayscale and apply a bilateral filter
    gray_scaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_scaled = cv2.bilateralFilter(gray_scaled, 15, 20, 20)

    # Detect edges using Canny edge detection
    edges = cv2.Canny(gray_scaled, 170, 200)
    cv2.imshow("Edged", edges)

    # Find contours
    contours, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    print(f"Total contours found: {len(contours)}")

    # Sort contours based on area and select the largest 30
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]
    Number_Plate_Contour = None

    # Loop over the contours to find the one that looks like a license plate
    for current_contour in contours:
        perimeter = cv2.arcLength(current_contour, True)
        approx = cv2.approxPolyDP(current_contour, 0.02 * perimeter, True)
        print(f"Contour with {len(approx)} points found")
        if len(approx) == 4:
            Number_Plate_Contour = approx
            break

    if Number_Plate_Contour is not None:
        print("Number plate contour detected")
        # Create a mask for the detected license plate contour
        mask = np.zeros(gray_scaled.shape, np.uint8)
        new_image1 = cv2.drawContours(mask, [Number_Plate_Contour], 0, 255, -1)
        new_image1 = cv2.bitwise_and(image, image, mask=mask)
        cv2.imshow("Number Plate", new_image1)

        # Convert the new image to grayscale and threshold it
        gray_scaled1 = cv2.cvtColor(new_image1, cv2.COLOR_BGR2GRAY)
        processed_img = cv2.threshold(gray_scaled1, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        cv2.imshow("Processed Number Plate", processed_img)

        # Extract text from the processed image using Tesseract
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(processed_img, config=custom_config)
        print("Number is:", text.strip())

    else:
        print("No number plate contour detected")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No file selected")

# Ensure that all OpenCV windows are closed properly
cv2.destroyAllWindows()
