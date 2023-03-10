import cv2
from pathlib import Path

image_path = Path('aula-01/images/len_std.png')
image      = cv2.imread(str(image_path))

cv2.imshow('Loaded Image', image)

cv2.waitKey(0)