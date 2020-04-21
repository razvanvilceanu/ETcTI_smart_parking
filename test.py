import cv2

lbls = ['standUp', 'front', 'lookU', 'lookF', 'lookDF', 'HandOnHipR']

img = cv2.imread("frame0.jpg")

h, w, c = img.shape

offset = 0

font = cv2.FONT_HERSHEY_SIMPLEX

for itr, word in enumerate(lbls):
    offset += int(h / len(lbls)) - 10
    cv2.putText(img, word, (20, offset), font, 1, (0, 255, 0), 3)

cv2.imwrite("road_OUT.jpg", img)
