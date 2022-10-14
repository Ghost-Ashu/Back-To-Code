import cv2
import mediapipe as mp 
import time
from datetime import datetime
from mediapipe.python.solutions.hands_connections import HAND_CONNECTIONS
from tkinter import *
mayur=Tk()
def may():
    ftip=[4,8,12,16,20]
    cap=cv2.VideoCapture(0)
    mphand=mp.solutions.hands
    hands=mphand.Hands()
    mpDraw=mp.solutions.drawing_utils
    j=0
    u=0
    while True:
        success,img=cap.read()
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results=hands.process(imgRGB)
        lst=[]
        if results.multi_hand_landmarks:
            for handlms in  results.multi_hand_landmarks:
                for id,lm in enumerate(handlms.landmark):
                    h,w,c=imgRGB.shape
                    cx=int(lm.x*w)
                    cy=int(lm.y*h)
                    lst.append([id,cx,cy])
                    #print(id,cx,cy)
                mpDraw.draw_landmarks(img,handlms,mphand.HAND_CONNECTIONS,mpDraw.DrawingSpec(color=(0,0,255)))
        sum=0
        if len(lst)!=0:
            if lst[ftip[0]][1]>lst[ftip[0]-1][1]:
                sum=sum+1
            for i in range (1,5):
                if lst[ftip[i]][2]<lst[ftip[i]-2][2]:
                        sum=sum+1
                else:
                        sum=sum+0  
                    
            #print(sum)
            if sum==5:
                print("open")
            elif sum==0:
                j=1
                k=0
            # print(time.time(),"*")
                #initial=time.time()-jk
                #print(initial)
                print("close")
                dt=time.strftime("%d/%m/%y_%H:%M")
            else:
                print("gasture not recognise")
            """if initial==int(time.time()):
                retval,im=cap.read()
                file="test_image.png"
                cv2.imwrite(file,im)"""

        else:
            print("no hand detect")
        if j:
            if k<150:
             cv2.putText(img,"pose",(10,20),cv2.FONT_HERSHEY_COMPLEX,1,(123,12,54))
            if 150==k:
                retval,imgs=cap.read()
                u=u+1
                print(dt)
                file="C:\\Users\\centiago\\Desktop\\hand_gastuaring-project\\gallary\\IMG-"+time.strftime("%d-%m-%y-%H-%M-%S")+".jpg"
                cv2.imwrite(file,imgs)
                cv2.putText(img,"CAPTURE",(60,60),cv2.FONT_HERSHEY_COMPLEX,1,(123,12,54))
                



            k=k+1
        cv2.imshow("image",img)
        if sum==2:
            break
        cv2.waitKey (1)
    
tex=Label(mayur,text="mayur;").grid(row=0,column=0)
e=Entry(mayur)
e.grid(row=0,column=1)
b=Button(mayur,text="click",padx=100,command=may)
b.grid(row=1,column=1)
ec=Entry()
ec.grid(row=2,column=0,columnspan=3,padx=10,pady=10)

mayur.mainloop()