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
        print('pic:',pic)
        place=pg.locateCenterOnScreen(pic)
        if place!=None:
            x,y=place
            print('pic_locate:',place)
            pg.moveTo(x,y, 2, pg.easeInOutQuad)
            time.sleep(2)
            pg.click()
            return 1
        else:
            print('pic',pic,'not on screen')
            return 0
        self.center()
    def is_on(pic):
        place=pg.locateCenterOnScreen(pic)
        if place!=None:
            return 1
        else:
            #print('pic',pic,'not on screen')
            return 0
    def down(self):
        pg.move(0,20,0.2)
    def arounder(self):
        sizex,sizey=pg.size()
        pg.moveTo(sizex-100,sizey-100,2,pg.easeInOutQuad)
        pg.moveTo(75,75,1,pg.easeInOutQuad)
        self.center()
    def click(self):
        pg.click()
    def quit(self):
        pass
    def videochange(self):
        a=self.find_mover('full_screen.png')
        b=self.find_mover('head.png')
        if a==0 or b==0:
            self.arounder()
            a=self.find_mover('opened_video.png')
            #self.arounder()
            if a==0:
                self.arounder()
                a=self.find_mover('closed_video.png')
        self.center()
    def center(self):
        sizex,sizey=pg.size()
        pg.moveTo(sizex//2,sizey//2,2,pg.easeInOutQuad)
    def entry(self):
        self.find_mover('head.png')
        self.find_mover('entry.png')
        if not microphone:
            self.find_mover('om.png')
        if not video:
            self.find_mover('ov.png')
        self.find_mover('num.png')
        self.down()
        self.click()
        self.typewrite(self.code)
        self.find_mover('name.png')
        self.down()
        self.click()
        self.typewrite(self.name)
        self.center()
if __name__=='__main__':
    print(int(time.time())^23054035)
    a=do('a','0')
    #a.find_mover('head.png')
    #a.arounder()
    a.videochange()
    #time.sleep(5)
    #a.videochange()
    #a.down()
