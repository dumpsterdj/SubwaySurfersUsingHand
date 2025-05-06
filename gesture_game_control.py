import cv2
import mediapipe as mp
import pyautogui
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
prev_pos = None
cooldown = 1  # time at which it responses to gesture
last_time = time.time()

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        lm = results.multi_hand_landmarks[0].landmark
        ix, iy = int(lm[8].x * w), int(lm[8].y * h)  # Index finger tip

        if prev_pos:
            dx = ix - prev_pos[0]
            dy = iy - prev_pos[1]

            threshold = 30 #senstivity for false triggers
            now = time.time()
            if now - last_time > cooldown:
                if dy < -threshold:
                    pyautogui.press('up')       # Jump
                    print("Jump")
                    last_time = now
                elif dy > threshold:
                    pyautogui.press('down')     # Duck
                    print("Duck")
                    last_time = now
                elif dx < -threshold:
                    pyautogui.press('left')     # Move left
                    print("Left")
                    last_time = now
                elif dx > threshold:
                    pyautogui.press('right')    # Move right
                    print("Right")
                    last_time = now

        prev_pos = (ix, iy)
        mp_draw.draw_landmarks(frame, results.multi_hand_landmarks[0], mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Gesture Control", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
