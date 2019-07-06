import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret, image = cap.read()
    height, width = image.shape[:2]

    #cropped left
    start_row, start_col = int(0), int(0)
    end_row, end_col = int(height), int(width * 1/3)
    cropped_left = image[start_row:end_row , start_col:end_col]

    #cropped middle
    start_row, start_col = int(0), int(width * 1/3)
    end_row, end_col = int(height), int(width * 2/3)
    cropped_middle = image[start_row:end_row , start_col:end_col]

    #cropped right
    start_row, start_col = int(0), int(width * 2/3)
    end_row, end_col = int(height), int(width)
    cropped_right = image[start_row:end_row , start_col:end_col]

    gray = cv2.cvtColor(cropped_left, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(cropped_middle, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(cropped_right, cv2.COLOR_BGR2GRAY)

    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )
    print("[INFO] for left Found {0} Faces!".format(len(faces)))

    for (x, y, w, h) in faces:
        cv2.rectangle(cropped_left, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    faces1 = faceCascade.detectMultiScale(
        gray1,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )
    print("[INFO] for right Found {0} Faces!".format(len(faces1)))

    for (x, y, w, h) in faces1:
        cv2.rectangle(cropped_middle, (x , y), (x + w , y + h), (0, 255, 0), 2)

    faces2 = faceCascade.detectMultiScale(
        gray2,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )

    print("[INFO] for right Found {0} Faces!".format(len(faces2)))

    for (x, y, w, h) in faces2:
        cv2.rectangle(cropped_right, (x , y), (x + w , y + h), (0, 255, 0), 2)

    cv2.imshow('left',cropped_left)
    cv2.imshow('middle',cropped_middle)
    cv2.imshow('right',cropped_right)
    cv2.imshow('img',image)
    
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()
cap.destryAllWindows()