import argparse

import cv2

# parse argument
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# reads the image
img = cv2.imread(args['image'])


# empty callback function for creating trackar
def callback(foo):
    pass


# create windows and trackbar
cv2.namedWindow('parameters')
cv2.createTrackbar('threshold1', 'parameters', 0, 255, callback)  # change the maximum to whatever you like
cv2.createTrackbar('threshold2', 'parameters', 0, 255, callback)  # change the maximum to whatever you like
cv2.createTrackbar('apertureSize', 'parameters', 0, 2, callback)
cv2.createTrackbar('L1/L2', 'parameters', 0, 1, callback)

while (True):
    # get threshold value from trackbar
    th1 = cv2.getTrackbarPos('threshold1', 'parameters')
    th2 = cv2.getTrackbarPos('threshold2', 'parameters')

    # aperture size can only be 3,5, or 7
    apSize = cv2.getTrackbarPos('apertureSize', 'parameters') * 2 + 3

    # true or false for the norm flag
    norm_flag = cv2.getTrackbarPos('L1/L2', 'parameters') == 1

    # print out the values
    print('')
    print('threshold1: {}'.format(th1))
    print('threshold2: {}'.format(th2))
    print('apertureSize: {}'.format(apSize))
    print('L2gradient: {}'.format(norm_flag))

    edge = cv2.Canny(img, th1, th2, apertureSize=apSize, L2gradient=norm_flag)
    cv2.imshow('canny', edge)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
