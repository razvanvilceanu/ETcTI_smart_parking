import cv2
import csv

with open('data/rois.csv', 'r', newline='') as inf:
    csvr = csv.reader(inf)
    rois = list(csvr)

rois = [[int(float(j)) for j in i] for i in rois]


def drawRectangle(img, a, b, c, d):
    sub_img = img[b:b + d, a:a + c]
    edges = cv2.Canny(sub_img, 350, 500)
    pix = cv2.countNonZero(edges)
    cv2.imshow('edges', edges)
    print(pix)
    if pix > 950 or pix < 120:
        cv2.rectangle(img, (a, b), (a + c, b + d), (0, 0, 255), 3)
    else:
        cv2.rectangle(img, (a, b), (a + c, b + d), (0, 255, 0), 3)


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    for i in range(len(rois)):
        drawRectangle(frame, rois[i][0], rois[i][1], rois[i][2], rois[i][3])
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
