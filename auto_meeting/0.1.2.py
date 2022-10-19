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
            pg.moveTo(x,y,1, pg.easeInOutQuad)
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
        pg.move(0,25,0.2)
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
        if a!=1:
            b=self.find_mover('head.png')
            a=self.find_mover('full_screen.png')
        else:
            b=1
        if a==1 or b==1:
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
        if not self.microphone:
            self.find_mover('om.png')
        if not self.video:
            self.find_mover('ov.png')
        self.find_mover('num.png')
        self.down()
        self.click()
        self.find_mover('del_name_num.png')
        pg.typewrite(self.code,0.1)
        self.find_mover('name.png')
        self.down()
        self.click()
        self.find_mover('del_name_num.png')
        pg.move(-20,0,1,pg.easeInOutQuad)
        self.click()
        pg.typewrite(self.name,0.1)
        self.center()
        #self.find_mover('join.png')
if __name__=='__main__':
    print(int(time.time())^23054035)
    a=do(input('填你滴名字:'),input('填你滴会议号:'))
    #a.find_mover('head.png')
    #a.arounder()
    #a.entry()
    #a.videochange()
    #time.sleep(5)
    a.videochange()
    #a.down()
