from math import hypot

import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import screen_brightness_control as abc

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2,min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils  #draw landmarks on the detected hands
cap = cv2.VideoCapture(0)
cv2.namedWindow('Hand Gesture', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Hand Gesture', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray_bgr = cv2.cvtColor(frame_gray, cv2.COLOR_GRAY2BGR)
    results = hands.process(cv2.cvtColor(frame_gray_bgr, cv2.COLOR_BGR2RGB))
    # List to store landmarks
    lmList = []#(x, y positions of key points)
    if results.multi_hand_landmarks:#Checks if any hand landmarks are detected. 
        for hand_landmarks in results.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):# Loops through each landmark in the hand, getting its id and its normalized coordinates (lm).
                h, w, _ = frame.shape#normalized coordinates
                cx, cy = int(lm.x * w), int(lm.y * h)#Converts the normalized coordinates to pixel coordinates (cx, cy)
                lmList.append([id, cx, cy])
            mp_drawing.draw_landmarks(frame_gray_bgr, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            # Calculate distance between thumb tip and index finger tip
            if len(lmList) >= 9:
                x1, y1 = lmList[4][1], lmList[4][2]#thumb tip4
                x2, y2 = lmList[8][1], lmList[8][2]#index finger tip8.
                length = hypot(x2 - x1, y2 - y1)
                # Adjust brightness based on distance
                if lmList[0][1] < w/2:  # left hand
                    brightness = np.interp(length, [15, 220], [0, 100])
                    abc.set_brightness(int(brightness))
                if lmList[0][1] > w/2:  # right hand 
                    if lmList[4][2] > lmList[8][2]:
                        pyautogui.press('volumeup')
                    else:
                        pyautogui.press('volumedown')
    cv2.putText(frame_gray_bgr, "Press 'q' to exit", (50, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('Hand Gesture', frame_gray_bgr)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
