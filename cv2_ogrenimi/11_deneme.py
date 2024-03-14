import cv2
import numpy as np 

canvas = np.zeros( (512,512,3), dtype=np.uint8   )

points1 = np.array([[[110, 200], [330, 200], [290,220] ,[100, 100]]], np.int32)

cv2.polylines(canvas, [points1], isClosed=False , color=(0,255,0), thickness=3)


cv2.imshow("canvas", canvas )

cv2.waitKey(0)

cv2.destroyAllWindows()