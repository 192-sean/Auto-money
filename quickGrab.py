import ImageGrab
import os
import time
import win32api
import win32con
import ImageOps
from numpy import *

class cord:
    load_career = (670, 465)
    start_battle = (795, 670)
    arena_1 = (140, 90)
    arena_2 = (140, 200)
    arena_3 = (140, 310)
    arena_4 = (140, 420)
    arena_5 = (140, 530)
    arena_6 = (365, 90)
    arena_7 = (365, 200)
    arena_8 = (365, 310)
    arena_9 = (365, 420)
    arena_10 = (365, 530)
    save_game = (870, 565)
    
#GLobals 
#--------
x_pad = 469 
y_pad = 128
 
def screenGrab():
    box = (x_pad+1,y_pad+1,x_pad+960,y_pad+720)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')

def screenJack():
    box = (x_pad+1,y_pad+1,x_pad+960,y_pad+720)
    im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
#'.png', 'PNG')
    return im  
    
def grab():
    box = (x_pad + 1,y_pad+1,x_pad+960,y_pad+720)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    return a  

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print "Click."          #completely optional. But nice for debugging purposes.
    
def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print 'left Down'
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print 'left release'
   
def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))
     
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x,y
    
def startGame():
    #location of first menu
    mousePos(cord.load_career)
    leftClick()
    time.sleep(3)
    
    mousePos(cord.start_battle)
    leftClick()
    time.sleep(3)
    
    mousePos(cord.arena_2)
    leftClick()
    time.sleep(3)
    
def main():
    time.sleep(5)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,-1060)
    time.sleep(3)
    startGame()
     
if __name__ == '__main__':
    main()