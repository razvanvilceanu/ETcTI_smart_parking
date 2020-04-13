import cv2
import csv

cap = cv2.VideoCapture(0)
suc, image= cap.read()

cv2.imwrite("frame0.jpg", image)     # save frame as JPEG file
img = cv2.imread("frame0.jpg")

rlist= []
r = cv2.selectROIs('whatever', img, showCrosshair=False, fromCenter=False)

rlist.append(r)
print(rlist)

with open('data/rois.csv', 'w', newline='') as outf:
  csvw = csv.writer(outf)
  csvw.writerows(rlist)

cap.release()
cv2.destroyAllWindows()