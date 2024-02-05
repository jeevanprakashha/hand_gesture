import cv2 
import serial
from cvzone.HandTrackingModule import HandDetector 
cap=cv2.VideoCapture(0) 
detector=HandDetector (detectionCon=0.5,maxHands=1) 
port="/dev/tty.usbserial-A50285BI" 
bt=serial.Serial (port,9600) 
while True:
    ret, frame=cap.read() 
    hands, frame=detector.findHands(frame) 
    if not hands:
      print ( "Nothing")
    else:
      hands1=hands [0]
      fingers detector.fingersUp (hands1)
      count=fingers.count (1)
      print (count)
      strinq='X(0}'.format(count)
      bt.write (string.encode ( ) )
   cv2. imshow ( "FRAME", frame)
   if cv2.waitKey (1) & OxFF == 27:
     break
cap. release ( )
cv2.destroyAllWindows ( )
