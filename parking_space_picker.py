import cv2
import pickle
import matplotlib.pyplot as plt

width = 27
height = 15

try:
    with open("CarParkPos", "rb") as f:
        posList = pickle.load(f)

except:
    posList = [] 


def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_FLAG_LBUTTON:
        posList.append((x,y))
    if events == cv2.EVENT_FLAG_RBUTTON:
        for i ,pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1+width and y1 < y < y1+height:
                posList.pop(i)
    with open("CarParkPos", "wb") as f:
        pickle.dump(posList, f)


while True:    
    img_path = "first_frame.png"
    img = cv2.imread(img_path)
    # print("posList: ",posList)
    
    for pos in posList:
        cv2.rectangle(img, pos, ((pos[0]+width),pos[1]+height),(255,0,0),2)
    
    cv2.imshow("img",img)
    cv2.setMouseCallback("img", mouseClick)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()