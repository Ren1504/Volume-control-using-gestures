import cv2
import handTrackingModule as htm
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

cap = cv2.VideoCapture(0)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
minvol , maxvol, _ = volume.GetVolumeRange()
vol = 0
dist = 0

while True:

    _,img = cap.read()
    
    landmarks = htm.findPosition(img,draw = False)

    if landmarks:

        x1,y1,x2,y2 = landmarks[4][1], landmarks[4][2],landmarks[8][1], landmarks[8][2]
        cv2.circle(img,(x1,y1),15,(255,0,0),cv2.FILLED)
        cv2.circle(img,(x2,y2),15,(255,0,0),cv2.FILLED)

        cx,cy = (x1+x2)//2, (y1+y2)//2

        cv2.circle(img,(cx,cy),15,(255,0,0),cv2.FILLED)

        cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)

        dist = ((x2-x1)**2+(y2-y2)**2)**0.5

        print(dist)
   
        if dist<5:
            cv2.circle(img,(cx,cy),15,(0,0,255),cv2.FILLED)
        
    vol = np.interp(dist,(3,45),[minvol,maxvol])
    volume.SetMasterVolumeLevel(vol,None)

    # img = htm.FindHands(img,draw)
    cv2.imshow("Video",img)
    cv2.waitKey(1)
