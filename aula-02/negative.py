import cv2
from pathlib import Path

image_path = Path('images/len_std.png')
image      = cv2.imread(str(image_path))

negative_image = ~image
back_image     = ~negative_image

cv2.imshow('Loaded Image', image)
cv2.imshow('Negative Image', negative_image)
cv2.imshow('Back Image', back_image)

cv2.waitKey(0)