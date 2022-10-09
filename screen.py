import pyautogui as p
p.FAILSAFE=False
import sys
def pre():
    p.keyDown('ctrl')
    p.keyDown('alt')
    p.keyDown('s')
    p.keyUp('ctrl')
    p.keyUp('alt')
    p.keyUp('s')
def mov():
    pre()
    p.moveTo(0,0,duration=3)
    p.mouseDown(button='left')
    p.moveTo(1600,900,duration=7.5)
    p.mouseUp(button='left')
def al():
    mov()
    p.moveTo(1550,25,duration=5)
    p.click()
def alll():
    al()
    p.moveTo(1475,25,duration=1)
    p.click()
    #sys.exit()

    
