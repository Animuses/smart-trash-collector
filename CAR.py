#!/usr/bin/python3
#通用调用库 By Animuses
#
import RPi.GPIO as GPIO
import time
import cv2
import os


#定义变量设定引脚接口与pwm
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LIN1 = 20
LIN2 = 21
LPWM = 16
RIN1 = 19
RIN2 = 26
RPWM = 13
BUZZER = 8
SERVO1 = 23
SERVO2 = 11
SERVO3 = 9
SERVO4 = 10
SERVO5 = 25
SERVO6 = 2
#初始化GPIO引脚和初始化PWM并复位
GPIO.setup(LPWM,GPIO.OUT)
GPIO.setup(LIN1,GPIO.OUT)
GPIO.setup(LIN2,GPIO.OUT)
GPIO.setup(RPWM,GPIO.OUT)
GPIO.setup(RIN1,GPIO.OUT)
GPIO.setup(RIN2,GPIO.OUT)
GPIO.setup(BUZZER,GPIO.OUT)
GPIO.setup(SERVO1,GPIO.OUT)
GPIO.setup(SERVO2,GPIO.OUT)
GPIO.setup(SERVO3,GPIO.OUT)
GPIO.setup(SERVO4,GPIO.OUT)
GPIO.setup(SERVO5,GPIO.OUT)
GPIO.setup(SERVO6,GPIO.OUT)
pwm_LPWM = GPIO.PWM(LPWM,2000)
pwm_RPWM = GPIO.PWM(RPWM,2000)
pwm_LPWM.start(0)
pwm_RPWM.start(0)
pwm_SERVO1 = GPIO.PWM(SERVO1,50)
pwm_SERVO2 = GPIO.PWM(SERVO2,50)
pwm_SERVO3 = GPIO.PWM(SERVO3,50)
pwm_SERVO4 = GPIO.PWM(SERVO4,50)
pwm_SERVO5 = GPIO.PWM(SERVO5,50)
pwm_SERVO6 = GPIO.PWM(SERVO6,50)
pwm_SERVO1.start(7.5)
pwm_SERVO2.start(7.5)
pwm_SERVO3.start(7.5)
pwm_SERVO4.start(7.5)
pwm_SERVO5.start(7.5)
pwm_SERVO6.start(7.5)

#初始化，设定引脚状态
#L为左轮，R为右轮，PWM为占空比，调速用，SERVO为舵机接口
def  init():
    print("Initialize success")
    beep(0.05)
    beep(0.05)
    #初始化完成后蜂鸣器响两声

#初始化结束

###############
##通用部件部分##
###############

#蜂鸣器响一声
def beep(time):
    GPIO.output(BUZZER, False)
    time.sleep(time)
    GPIO.output(BUZZER, True)
    time.sleep(0.05)


#关机 完成后长响一声
def shutdown():
    beep(0.1)
    GPIO.cleanup()


###############
##小车运动部分##
###############

#停车
def stop():
    GPIO.output(LIN1, False)
    GPIO.output(LIN2, False)
    GPIO.output(RIN1, False)
    GPIO.output(RIN2, False)

#前进
def forward(speed):
    pwm_LPWM.ChangeDutyCycle(speed)
    pwm_RPWM.ChangeDutyCycle(speed)
    GPIO.output(LIN1, True)
    GPIO.output(LIN2, False)
    GPIO.output(RIN1, True)
    GPIO.output(RIN2, False)

#后退
def backward(speed):
    pwm_LPWM.ChangeDutyCycle(speed)
    pwm_RPWM.ChangeDutyCycle(speed)
    GPIO.output(LIN1, False)
    GPIO.output(LIN2, True)
    GPIO.output(RIN1, False)
    GPIO.output(RIN2, True)

#原地左转
def left_spin(speed):
    pwm_LPWM.ChangeDutyCycle(speed)
    pwm_RPWM.ChangeDutyCycle(speed)
    GPIO.output(LIN1, False)
    GPIO.output(LIN2, True)
    GPIO.output(RIN1, True)
    GPIO.output(RIN2, False)

#原地右转
def right_spin(speed):
    pwm_LPWM.ChangeDutyCycle(speed)
    pwm_RPWM.ChangeDutyCycle(speed)
    GPIO.output(LIN1, True)
    GPIO.output(LIN2, False)
    GPIO.output(RIN1, False)
    GPIO.output(RIN2, True)

###############
##舵机控制部分##
##目前尚在测试##
###############

#扫帚开
def sweep_open():
    pwm_SERVO1.ChangeDutyCycle(2.5)

#扫帚关
def sweep_close():
    pwm_SERVO1.ChangeDutyCycle(12.5)

#用不上的代码注释掉了
'''
#角度转换为PWM，范围：0-270
def Servo_angle(angle):
    duty = (angle/270+0.25)*10
    return(duty)

#舵机旋转至特定角度
def Servo_rotate(pwm_servo,target):
    pwm_servo.ChangeDutyCycle(target)

#舵机正转（仅适用于遥控）
def Servo_pos(pwm_servo,angle_now):
    for angle_now in range(2.5,12.5):
        angle_now=angle_now+0.1
        Servo_rotate(pwm_servo,angle_now)

#舵机反转（仅适用于遥控）
def Servo_neg(pwm_servo,angle_now):
    for angle_now in range(2.5,12.5):
        angle_now=angle_now-0.1
        Servo_rotate(pwm_servo,angle_now)
'''


###############
##视觉识别部分##
###############
#By Qing

"""
battery     0
bottle      1
cup         2
orange      3
paper       4
"""
#发送函数
def send(m):
    import serial
    serial = serial.Serial('COM7', 115200, timeout=2)  # 连接串口
    if serial.isOpen():
        print('串口已打开')
        data = b'm\r\n'  # 发送的数据
        serial.write(data)  # 串口写数据
        print('You Send Data:', data)

    while True:
        data = serial.read(20)  # 串口读20位数据
        if data != b'':
            print('receive data is :', data)
            break
        else:
            print('串口未打开')

 # 关闭串口
    serial.close()
    if serial.isOpen():
        print('串口未关闭')
    else:
        print('串口已关闭')

#开始识别
def recognize(calsses):
  cap = cv2.VideoCapture(1)
  i = 2
  z = 0 # x轴向上移动多少
  while(True):  # 第一个垃圾区域的循环
    ret, frame = cap.read()
    cv2.imwrite("C:\Users\qing\Desktop\yolov5-master\\" + str(i) + ".jpg", frame) # 保存图片
    ver = os.system('python detect.py --source 2.jpg --weights="weights/best.pt" --agnostic-nms --save-txt --exist-ok')  # 检测电池
    try:
        with open("C:\\Users\\qing\\Desktop\\yolov5-master\\runs\\detect\\exp\\labels\\2.txt", "r") as f:  # 打开文件
            data = f.readline()  # 读取文件
            data = data.split() # 转换为数组
            print(data)
            x = data[1]
            y = data[2] # 读取坐标
            x = float(x)*640
            y = float(y)*480
            x = int(x-320)
            y = int(480-y-z) # 坐标系变换
            if x<0:
                data = x*1000-y
                data = 1000000-data # data第一位的1表负
            else:
                data = x*1000+y
                data = 2000000+data # data第一位的2表正
        send(data) # 发送坐标
        print("中心点坐标：",data)
        print("中心点坐标：",x,y)
        time.sleep(10)
    except:
        break
    os.remove("2.jpg") # 删除这次检测的图片
    os.remove("C:\\Users\\qing\\Desktop\\yolov5-master\\runs\\detect\\exp\\labels\\2.txt") # 删除这次检测的数据
    os.remove("C:\\Users\\qing\\Desktop\\yolov5-master\\runs\\detect\\exp\\2.jpg") # 删除这次检测的图片


#结束
