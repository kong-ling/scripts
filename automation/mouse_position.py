import  os
import  sys
import  time
import pyautogui as pag

t32_position=[1045, 903]
try:
    while True:
        print("Press Ctrl-C to end")
        screenWidth, screenHeight = pag.size()  #获取屏幕的尺寸
        print(screenWidth,screenHeight)
        x,y = pag.position()   #获取当前鼠标的位置

        posStr = "Position:" + str(x).rjust(4)+','+str(y).rjust(4)
        print(posStr)
        time.sleep(0.2)
        os.system('cls')   #清楚屏幕
except KeyboardInterrupt:
    print('end....')

#pag.click(t32_position[0], t32_position[1])
#pag.typewrite('os pythonw C:\posv_cv_script-scripts\CH340\ch340.py\n', 0.01)
