import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
image = cv2.imread('object_detection.jpg')
bbox, label, conf = cv.detect_common_objects(image)
print(label)
output_image = draw_bbox(image, bbox, label, conf)
cv2.imshow("object_detection", output_image)
cv2.waitKey()
cv2.destroyAllWindows()
