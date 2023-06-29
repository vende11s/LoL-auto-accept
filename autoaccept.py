import numpy
import cv2
import time
import pyautogui

def isTemplateInImage(template, image):
    result = cv2.matchTemplate(image, template, cv2.TM_SQDIFF_NORMED)
    min_val = cv2.minMaxLoc(result)[0]
    thr = 10e-6

    return min_val <= thr

def findTemplateInImage(template, image):
    if not isTemplateInImage(template, image):
        return None,None
    
    result = cv2.matchTemplate(template, image, cv2.TM_SQDIFF_NORMED)

    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    MPx,MPy = mnLoc
    height, width = template.shape[:2]
    
    MPx += width/2
    MPy += height/2

    return MPx, MPy

def click(x,y):
    (cur_x, cur_y) = pyautogui.position()
    # Your automated click
    pyautogui.click(x, y)
    # Move back to where the mouse was before click
   # pyautogui.moveTo(cur_x, cur_y)

def clickWhenTemplateOnScreen():
    templates = [cv2.imread('resources/1600x900.png'),
                 cv2.imread('resources/1280x720.png'),
                 cv2.imread('resources/1024x576.png')]
    while True:
        screen = pyautogui.screenshot()
        cv_screen = cv2.cvtColor(numpy.array(screen),cv2.COLOR_RGB2BGR)

        for template in templates:
            z+=1
            x,y = findTemplateInImage(template, cv_screen)

            if not x == None:
                click(x,y)
                exit()
            
        print('not found')
        time.sleep(1)

clickWhenTemplateOnScreen()