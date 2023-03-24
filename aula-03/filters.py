import cv2
from numpy import array
from pathlib import Path

image_path = Path('images/len_std.png')
image      = cv2.imread(str(image_path), 0)

cv2.imshow('Loaded Image', image)

low_pass = cv2.blur(image,(3,3))

cv2.imshow('Low Pass Filter', low_pass)

mask_4 = array([[0, -1, 0],
                [-1,  4, -1],
                [0, -1, 0]])

mask_8 = array([[-1, -1, -1],
                [-1,  8, -1],
                [-1, -1, -1]])

high_pass_4 = cv2.filter2D(low_pass, ddepth=None, kernel=mask_4)
high_pass_8 = cv2.filter2D(low_pass, ddepth=None, kernel=mask_8)

cv2.imshow('High Pass Filter 4', high_pass_4)

cv2.imshow('High Pass Filter 8', high_pass_8)

cv2.waitKey(0)
cv2.destroyAllWindows()