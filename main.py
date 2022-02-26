# -*- coding:utf-8 -*-
"""
Author: Vercent
Date:2022 年 01 月 23 日 
Title:
"""
import cv2
import numpy as np
from gui_buttons import Buttons

# Initialize buttons
button = Buttons()
button.add_button("Person", 20, 20)
button.add_button("Remote", 20, 100)
button.add_button("Book", 20, 180)
button.add_button("Keyboard", 20, 260)
button.add_button("Cell Phones", 20, 340)

# Opencv DNN
net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1 / 255)

# Load class lists
classes = []
with open("dnn_model/classes.txt", "r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append((class_name))

# Initialize camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


# Full HD 1920x1080


def click_button(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        button.button_click(x, y)


# Create a window
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", click_button)

while True:
    # Get frames
    ret, frame = cap.read()

    # Get active buttons list
    active_buttons = button.active_buttons_list()

    # Object Detection
    (class_ids, scores, bboxes) = model.detect(frame)
    for class_id, score, bbox in zip(class_ids, scores, bboxes):
        (x, y, w, h) = bbox

        class_name = classes[class_id]

        if class_name in active_buttons:
            cv2.putText(frame, str(class_name), (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (200, 0, 50), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (200, 0, 50), 3)

    # Display Buttons
    button.display_buttons(frame)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)  # 0表示设置冻结帧

    # Enter 'tab' button to break
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()