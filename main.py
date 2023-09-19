import cv2
import time
import os
import HandTrackingModule as htm

hCam, wCam = 480, 640

cap = cv2.VideoCapture(0)
cap.set(4, hCam)
cap.set(3, wCam)

detector = htm.handDetector(detectionCon = 0)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    posList = detector.findPosition(img, draw=False)
    # print(posList)
    
    # tips = [4, 8, 12, 16, 20]
    
    if len(posList) != 0:
        # fingers = []
        

        # if posList[tips[0]][1] > posList[tips[0]-1][1]:
        #     fingers.append(1)
        # else:
        #     fingers.append(0)
                
        # for id in range(1,5):
        #     if posList[tips[id]][2] < posList[tips[id]-2][2]:
        #         fingers.append(1)
        #     else:
        #         fingers.append(0)
                
        # print(fingers)
        
        # totalfingers = fingers.count(1)
        # print(totalfingers)
        
        result = ""
        fingers = []
        
        finger_mcp = [5,9,13,17]
        finger_dip = [6,10,14,18]
        finger_pip = [7,11,15,19]
        finger_tip = [8,12,16,20]
        
        for id in range(4):
            if(posList[finger_tip[id]][1]+ 25  < posList[finger_dip[id]][1] and posList[16][2]<posList[20][2]):
                fingers.append(0.25)
            elif(posList[finger_tip[id]][2] > posList[finger_dip[id]][2]):
                fingers.append(0)
            elif(posList[finger_tip[id]][2] < posList[finger_pip[id]][2]): 
                fingers.append(1)
            elif(posList[finger_tip[id]][1] > posList[finger_pip[id]][1] and posList[finger_tip[id]][1] > posList[finger_dip[id]][1]): 
                fingers.append(0.5)
                
        print(fingers)
        # print(posList)
            
        if(posList[3][2] > posList[4][2]) and (posList[3][1] > posList[6][1])and (posList[4][2] < posList[6][2]) and fingers.count(0) == 4:
            result = "A"
            
        elif(posList[3][1] > posList[4][1]) and fingers.count(1) == 4:
            result = "B"
        
        elif(posList[3][1] > posList[6][1]) and fingers.count(0.5) >= 1 and (posList[4][2]> posList[8][2]):
            result = "C"
            
        elif(fingers[0]==1) and fingers.count(0) == 3 and (posList[3][1] > posList[4][1]):
            result = "D"
        
        elif (posList[3][1] < posList[6][1]) and fingers.count(0) == 4 and posList[12][2]<posList[4][2]:
            result = "E"

        elif (fingers.count(1) == 3) and (fingers[0]==0) and (posList[3][2] > posList[4][2]):
            result = "F"

        elif(fingers[0]==0.25) and fingers.count(0) == 3:
            result = "G"

        elif(fingers[0]==0.25) and(fingers[1]==0.25) and fingers.count(0) == 2:
            result = "H"
        
        elif (posList[4][1] < posList[6][1]) and fingers.count(0) == 3:
            if (len(fingers)==4 and fingers[3] == 1):
                result = "I"
        
        elif (posList[4][1] < posList[6][1] and posList[4][1] > posList[10][1] and fingers.count(1) == 2):
            result = "K"
            
        elif(fingers[0]==1) and fingers.count(0) == 3 and (posList[3][1] < posList[4][1]):
            result = "L"
        
        elif (posList[4][1] < posList[16][1]) and fingers.count(0) == 4:
            result = "M"
        
        elif (posList[4][1] < posList[12][1]) and fingers.count(0) == 4:
            result = "N"
            
        # elif(posList[3][1] > posList[6][1]) and (posList[3][2] < posList[6][2]) and fingers.count(0.5) >= 1:
        #     result = "O"
        
        elif (posList[4][1] > posList[12][1]) and posList[4][2]<posList[6][2] and fingers.count(0) == 4:
            result = "T"

        elif (posList[4][1] > posList[12][1]) and posList[4][2]<posList[12][2] and fingers.count(0) == 4:
            result = "S"

        
        elif(posList[4][2] < posList[8][2]) and (posList[4][2] < posList[12][2]) and (posList[4][2] < posList[16][2]) and (posList[4][2] < posList[20][2]):
            result = "O"
        
        elif(fingers[2] == 0)  and (posList[4][2] < posList[12][2]) and (posList[4][2] > posList[6][2]):
            if (len(fingers)==4 and fingers[3] == 0):
                result = "P"
        
        elif(fingers[1] == 0) and (fingers[2] == 0) and (fingers[3] == 0) and (posList[8][2] > posList[5][2]) and (posList[4][2] < posList[1][2]):
            result = "Q"
        
        # elif(posList[10][2] < posList[8][2] and fingers.count(0) == 4 and posList[4][2] > posList[14][2]):
        #     result = "Q" 
            
        elif(posList[8][1] < posList[12][1]) and (fingers.count(1) == 2) and (posList[9][1] > posList[4][1]):
            result = "R"
            
        # elif (posList[3][1] < posList[6][1]) and fingers.count(0) == 4:
        #     result = "S"
            
        elif (posList[4][1] < posList[6][1] and posList[4][1] < posList[10][1] and fingers.count(1) == 2 and posList[3][2] > posList[4][2] and (posList[8][1] - posList[11][1]) <= 50):
            result = "U"
            
        elif (posList[4][1] < posList[6][1] and posList[4][1] < posList[10][1] and fingers.count(1) == 2 and posList[3][2] > posList[4][2]):
            result = "V"
        
        elif (posList[4][1] < posList[6][1] and posList[4][1] < posList[10][1] and fingers.count(1) == 3):
            result = "W"
        
        elif (fingers[0] == 0.5 and fingers.count(0) == 3 and posList[4][1] > posList[6][1]):
            result = "X"
        
        elif(fingers.count(0) == 3) and (posList[3][1] < posList[4][1]):
            if (len(fingers)==4 and fingers[3] == 1):
                result = "Y"
        
        # if(posList[4][1] < posList[])

        
        cv2.rectangle(img, (28,255), (178, 425), (0, 225, 0), cv2.FILLED)
        cv2.putText(img, str(result), (55,400), cv2.FONT_HERSHEY_COMPLEX,5, (255,0,0), 15)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)