import cv2
from numpy import zeros, int16
from math import floor
from pathlib import Path

MATIX_SIZE = 5

image_path = Path('images/1280px-Hereditary_elliptocytosis.jpg')
image      = cv2.imread(str(image_path), 0)

cv2.namedWindow('Loaded Image', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Loaded Image', image)

low_pass = cv2.blur(image,(5,5))

cv2.namedWindow('Low Pass Filter', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Low Pass Filter', low_pass)

kernel = zeros((MATIX_SIZE, MATIX_SIZE), int16)

kernel = kernel - 1

m = floor(len(kernel)/2)

kernel[m][m] = MATIX_SIZE * MATIX_SIZE - 1

high_pass = cv2.filter2D(low_pass, ddepth=None, kernel=kernel)

cv2.namedWindow('High Pass Filter', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('High Pass Filter', high_pass)

normalized_image = cv2.normalize(high_pass, None, 0, 255, cv2.NORM_MINMAX)

cv2.namedWindow('Normalized', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Normalized', normalized_image)

ret, binarized_image = cv2.threshold(normalized_image, 45, 255, cv2.THRESH_BINARY)

cv2.namedWindow('Binarized image', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Binarized image', binarized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()