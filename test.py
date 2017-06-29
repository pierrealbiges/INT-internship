print('hello world')
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
print(cap)
while(True):
	ret, frame = cap.read()
	print(ret, frame)

	cv2.imshow('test',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
