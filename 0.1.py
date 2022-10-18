import pyautogui as pg
import time
import pyperclip as pc
pg.PAUSE=0.5
class do:
    def __init__(self,name,code,microphone=False,video=False):
        self.name=name
        self.code=code
        self.microphone=microphone
        self.video=video
    def find_mover(self,pic):
        place=pg.locateCenterOnScreen(pic)
        if place!=None:
            x,y=place
            print('pic_locate:',place)
            pg.moveTo(x,y, 2, pg.easeInOutQuad)
            time.sleep(3)
            pg.click()
            return 1
        else:
            print('pic',pic,'not on screen')
            return 0
    def is_on(pic):
        place=pg.locateCenterOnScreen(pic)
        if place!=None:
            return 1
        else:
            #print('pic',pic,'not on screen')
            return 0
    def down(self):
        pg.move(0,15,0.2)
    def arounder(self):
        sizex,sizey=pg.size()
        pg.moveTo(sizex-100,sizey-100,2,pg.easeInOutQuad)
        pg.moveTo(75,75,1,pg.easeInOutQuad)
    def click(self):
        pg.click()
    def quit(self):
        pass
    def videochange(self):
        self.find_mover('full_screen.png')
        self.find_mover('head.png')
        self.arounder()
        a=self.find_mover('opened_video.png')
        self.arounder()
        if a==0:
            a=self.find_mover('closed_video.png')
