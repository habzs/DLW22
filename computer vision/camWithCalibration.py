from inspect import getcomments
import numpy as np
import cv2
from mss import mss
from PIL import Image

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('key.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://escendotwo-default-rtdb.firebaseio.com'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
table1 = db.reference('vacant/one/')
table2 = db.reference('vacant/two/')
table3 = db.reference('vacant/three/')
table4 = db.reference('vacant/four/')

table1.set({
    'status': 0}
)
table2.set({
    'status': 0}
)
table3.set({
    'status': 0}
)
table4.set({
    'status': 0}
)

bounding_box = {'top': 100, 'left': 0, 'width': 1280, 'height': 720}

TABL1_X1 = 335
TABL1_Y1 = 620
TABL2_X1 = 1077
TABL2_Y1 = 354
TABL3_X1 = 1077
TABL3_Y1 = 854
TABL4_X1 = 1740
TABL4_Y1 = 728
RADIUS = 62

sct = mss()
kernel = np.ones((5, 5), np.uint8)
sct_img = sct.grab(bounding_box)
tableNumber = [0, 0, 0, 0]
calibrated = 0
startCount = 0
alteredImage = sct_img


def removeSpeckles(maskedImage):
    opening = cv2.morphologyEx(maskedImage, cv2.MORPH_OPEN, kernel)
    return opening


def getColorMask(img, cali):
    # lB = np.array([101, 150, 124])
    # uB = np.array([96, 130, 215])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    if (cali == 0):
        # blue objects
        lB = np.array([90, 75, 75])
        uB = np.array([130, 255, 255])
    else:
        # yellow objects
        lB = np.array([20, 100, 100])
        uB = np.array([30, 255, 255])

    mask = cv2.inRange(hsv, lB, uB)
    result = cv2.bitwise_and(img, img, mask=mask)

    return mask


def findContoursAndPrintCoordinatesOnScreen():
    # find contours in the thresholded image
    global alteredImage
    global tableNumber, startCount
    global TABL1_X1, TABL1_Y1, TABL2_X1, TABL2_Y1, TABL3_X1, TABL3_Y1, TABL4_X1, TABL4_Y1, RADIUS

    cnts = cv2.findContours(
        masked.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    # cnts = cv2.findContours(masked.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
    # loop over the contours
    for c in cnts:
        # compute the center of the contour
        M = cv2.moments(c)

        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        # draw the contour and center of the shape on the image
        alteredImage = cv2.drawContours(
            np.array(alteredImage), [c], -1, (0, 255, 0), 2)
        alteredImage = cv2.circle(
            np.array(alteredImage), (cX, cY), 7, (255, 255, 255), -1)

        if (pow((TABL1_X1 - cX), 2) + pow((TABL1_Y1 - cY), 2) < pow(RADIUS, 2)):
            tableNumber[0] += 1
            # print("table 1 detected")
        if (pow((TABL2_X1 - cX), 2) + pow((TABL2_Y1 - cY), 2) < pow(RADIUS, 2)):
            tableNumber[1] += 1
            # print("table 2 detected")
        if (pow((TABL3_X1 - cX), 2) + pow((TABL3_Y1 - cY), 2) < pow(RADIUS, 2)):
            tableNumber[2] += 1
            # print("table 3 detected")
        if (pow((TABL4_X1 - cX), 2) + pow((TABL4_Y1 - cY), 2) < pow(RADIUS, 2)):
            tableNumber[3] += 1
            # print("table 4 detected")

        # cv2.putText(img, "center", (cX - 20, cY - 20),
        #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        string = str(cX) + " " + str(cY)

        alteredImage = cv2.putText(np.array(
            alteredImage), string, (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # show the image
        # cv2.imshow("Image", np.array(alteredImage))
        # cv2.waitKey(0)

# calibrate tables


def calibrateTable():
    # find contours in the thresholded image
    global sct_img, calibrated
    global tableNumber
    global TABL1_X1, TABL1_Y1, TABL2_X1, TABL2_Y1, TABL3_X1, TABL3_Y1, TABL4_X1, TABL4_Y1

    orangeImage = sct_img

    cnets = cv2.findContours(
        tableMask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    # cnts = cv2.findContours(masked.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]

    # loop over the contours
    for c in cnets:
        # compute the center of the contour
        M = cv2.moments(c)

        try:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            # draw the contour and center of the shape on the image
            orangeImage = cv2.drawContours(
                np.array(orangeImage), [c], -1, (0, 255, 0), 2)
            orangeImage = cv2.circle(
                np.array(orangeImage), (cX, cY), 7, (255, 255, 255), -1)

            if (cX < 538):
                TABL1_X1 = cX
                TABL1_Y1 = cY
            elif (cY < 360):
                TABL2_X1 = cX
                TABL2_Y1 = cY
            elif (cY > 460):
                TABL3_X1 = cX
                TABL3_Y1 = cY
            elif (cX > 743):
                TABL4_X1 = cX
                TABL4_Y1 = cY

            string = str(cX) + " " + str(cY)

            orangeImage = cv2.putText(np.array(
                orangeImage), string, (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        except:
            print("crashed")

        calibrated = 1
        print("calibrated!")
        # show the image
        cv2.imshow("Image", np.array(orangeImage))
        # cv2.waitKey(0)


masked = getColorMask(np.array(sct_img), 0)
masked = removeSpeckles(masked)

tableMask = getColorMask(np.array(sct_img), 1)
tableMask = removeSpeckles(tableMask)

while True:
    sct_img = sct.grab(bounding_box)
    masked = getColorMask(np.array(sct_img), 0)
    masked = removeSpeckles(masked)

    if (calibrated == 0):
        alteredImage = cv2.putText(np.array(sct_img), "PRESS `C` TO CALIBRATE", (
            50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_4)
    else:
        alteredImage = cv2.putText(np.array(sct_img), "CALIBRATED", (
            50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_4)

    if (tableNumber[0] > 0):
        table1.set({
            'status': 1
        })
    else:
        table1.set({
            'status': 0
        })

    if (tableNumber[1] > 0):
        table2.set({
            'status': 1
        })
    else:
        table2.set({
            'status': 0
        })

    if (tableNumber[2] > 0):
        table3.set({
            'status': 1
        })
    else:
        table3.set({
            'status': 0
        })

    if (tableNumber[3] > 0):
        table4.set({
            'status': 1
        })
    else:
        table4.set({
            'status': 0
        })

    if (cv2.waitKey(99) == ord('c')):
        tableMask = getColorMask(np.array(sct_img), 1)
        tableMask = removeSpeckles(tableMask)

        calibrateTable()
        print("X1: " + str(TABL1_X1) + " Y1: " + str(TABL1_Y1))
        print("X2: " + str(TABL2_X1) + " Y2: " + str(TABL2_Y1))
        print("X3: " + str(TABL3_X1) + " Y3: " + str(TABL3_Y1))
        print("X4: " + str(TABL4_X1) + " Y4: " + str(TABL4_Y1))

    if (calibrated == 1):
        tableNumber[0] = tableNumber[1] = tableNumber[2] = tableNumber[3] = 0
        findContoursAndPrintCoordinatesOnScreen()

    cv2.imshow('screen', np.array(alteredImage))

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
