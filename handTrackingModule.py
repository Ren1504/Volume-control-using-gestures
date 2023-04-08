import cv2
import mediapipe as mp


mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence = 0.7)
mpDraw = mp.solutions.drawing_utils


def FindHands(img, draw = True):
    rgb_image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_image)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            if draw:
                mpDraw.draw_landmarks(img, hand_landmarks, mpHands.HAND_CONNECTIONS)
    
    return img

def findPosition(img,handNO = 0, draw = False):
            lmList = []
            rgb_image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            results = hands.process(rgb_image)

            if results.multi_hand_landmarks:
                  myHand = results.multi_hand_landmarks[handNO]
                  for id, landmarks in enumerate(myHand.landmark):
                        h,w,c = img.shape
                        cx,cy = int(landmarks.x * w), int(landmarks.y * h)
                        lmList.append([id,cx,cy])

                        if draw:
                              cv2.circle(img,(cx,cy),15,(0,255,255), cv2.FILLED)
            return lmList

