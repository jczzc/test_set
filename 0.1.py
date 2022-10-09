import pyautogui as p
import screen as s
p.FAILSAFE=False
name=input('name:')
room=input('room:')
is_pw=False
if input('is_password:')=='t':
    password=input('password:')
    is_pw=True
h=input('enter hour:')
m=input('enter minute:')
s.alll()
p.moveTo(747,116,duration=2)
p.click()
p.moveTo(664,245,duration=1)
p.click()
p.moveTo(914,250,duration=1)
p.click()
p.moveTo(698,249,duration=1)
p.click()
p.typewrite(room,0.25)
p.moveTo(945,317,duration=0.1)
p.click()
p.moveTo(698,314,duration=1)
p.click()
import pyperclip as c
c.copy(name)
p.hotkey('ctrl','v')
p.moveTo(644,459,duration=2)
p.click()
p.moveTo(814,749,duration=1)
p.click()
if is_pw:
    p.moveTo(786,450,duration=1)
    p.click()
    p.typewrite(password,0.3)
    p.moveTo(883,506,duration=1)
    p.click()
