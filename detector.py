import cv2
import csv

with open('data/rois.csv','r', newline='') as inf:
  csvr=csv.reader(inf)
  rois=list(csvr)
  rois=rois[0]

print(rois)
print(rois[0][3])
