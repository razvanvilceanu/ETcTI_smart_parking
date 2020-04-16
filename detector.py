import cv2
import csv

def drawRectangle(img, a, b, c, d):
    sub_img = img[b:b + d, a:a + c]
    edges = cv2.Canny(sub_img, lowThreshold, highThreshold)
    pix = cv2.countNonZero(edges)
    cv2.imshow('edges', edges)
    if pix in range(min, max):
        cv2.rectangle(img, (a, b), (a + c, b + d), (0, 0, 255), 3)
    else:
        cv2.rectangle(img, (a, b), (a + c, b + d), (0, 255, 0), 3)


def callback(foo):
    pass


with open('data/rois.csv', 'r', newline='') as inf:
    csvr = csv.reader(inf)
    rois = list(csvr)

rois = [[int(float(j)) for j in i] for i in rois]

cv2.namedWindow('parameters')
cv2.createTrackbar('Threshold1', 'parameters', 0, 700, callback)
cv2.createTrackbar('Threshold2', 'parameters', 0, 700, callback)
cv2.createTrackbar('Min pixels', 'parameters', 0, 700, callback)
cv2.createTrackbar('Max pixels', 'parameters', 0, 700, callback)

# Select the video source; 0 - integrated webcam; 1 - external webcam
pix = 0
VIDEO_SOURCE = 0
cap = cv2.VideoCapture(VIDEO_SOURCE)
while True:
    ret, frame = cap.read()
    min = cv2.getTrackbarPos('Min pixels', 'parameters')
    max = cv2.getTrackbarPos('Max pixels', 'parameters')
    lowThreshold = cv2.getTrackbarPos('Threshold1', 'parameters')
    highThreshold = cv2.getTrackbarPos('Threshold2', 'parameters')
    print(highThreshold, " ", lowThreshold, pix)
    for i in range(len(rois)):
        drawRectangle(frame, rois[i][0], rois[i][1], rois[i][2], rois[i][3])
    cv2.imshow('frame', frame)

    # Listen for 'Q' key to stop the stream
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
