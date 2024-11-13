from gpiozero import Button
from gpiozero import LED
from time import sleep
from signal import pause

btn = Button(17)     # 轻触按键管脚
p_R = LED(18)        # 红色LED管脚
p_G = LED(27)        # 绿色LED管脚

def pressed():
    print('*****************************************') 
    print('* makerobo Raspberry Kit Button Pressed!*') 
    print('*****************************************')
    p_R.on()  # 打开红色LED
    p_G.off() # 关闭绿色LED

def released():
    print("button was released")
    p_R.off()   # 关闭红色LED
    p_G.on()    # 打开绿色LED

# 当按钮被按下时，调用pressed函数
btn.when_pressed = pressed
# 当按钮被释放时，调用released函数
btn.when_released = released

# 循环函数	
def makerobo_loop():
    pause()

# 释放资源
def makerobo_destroy():
    p_R.close()
    p_G.close()

# 程序入口
if __name__ == '__main__':
	try:
		makerobo_loop()        #  调用循环函数
	except KeyboardInterrupt:  #  当按下Ctrl+C时，将执行destroy()子程序。
		makerobo_destroy()     #  释放资源