import cv2
from pathlib import Path

image_path = Path('images/len_std.png')
image      = cv2.imread(str(image_path))

gray_scale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

negative_image = ~gray_scale_image
back_image     = ~negative_image

cv2.imshow('Loaded Image', gray_scale_image)
cv2.imshow('Negative Image', negative_image)
cv2.imshow('Back Image', back_image)

cv2.waitKey(0)