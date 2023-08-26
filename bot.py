import pyautogui as pg
import time


for i in range(3):
    pg.moveTo(622,755)
    pg.click()
    time.sleep(4)
    pg.doubleClick(622,755)
    time.sleep(4)
    pg.click(967,801)
    pg.typewrite('nice')
    pg.typewrite(['enter'])
    time.sleep(4)
    pg.click(863,486)