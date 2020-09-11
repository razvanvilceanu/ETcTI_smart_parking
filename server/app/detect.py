import cv2
import csv
import os

class spots:
    loc=0

file= "../../data/rois.csv"
class Detect:
    def load_data(path):
        with open(path, 'r', newline='') as inf:
            csvr = csv.reader(inf)
            rois = list(csvr)
        rois = [[int(float(j)) for j in i] for i in rois]
        return rois

    def draw_rectangles(img,a,b,c,d, lowThreshold, highTreshold):
        sub_img= img[b:b+d, a:a+c]
        edges = cv2.Canny(img, lowThreshold, highTreshold)



if __name__ == '__main__':
    print(Detect.load_data(file))
