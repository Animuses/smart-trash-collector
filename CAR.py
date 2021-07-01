#!/usr/bin/python
#通用调用库 By Animuses
import RPi.GPIO as GPIO
import time

#初始化，设定引脚状态
def  init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    global LIN1,LIN2,RIN1,RIN2,LPWM,RPWM,BUZZER,pwm_LPWM,pwm_RPWM
    LIN1 = 20
    LIN2 = 21
    LPWM = 16
    RIN1 = 19
    RIN2 = 26
    RPWM = 13
    BUZZER = 8
    GPIO.setup(LPWM,GPIO.OUT)
    GPIO.setup(LIN1,GPIO.OUT)
    GPIO.setup(LIN2,GPIO.OUT)
    GPIO.setup(RPWM,GPIO.OUT)
    GPIO.setup(RIN1,GPIO.OUT)
    GPIO.setup(RIN2,GPIO.OUT)
    GPIO.setup(BUZZER,GPIO.OUT)
    pwm_LPWM = GPIO.PWM(LPWM,2000)
    pwm_RPWM = GPIO.PWM(RPWM,2000)
    pwm_LPWM.start(0)
    pwm_RPWM.start(0)
    beep()
    #初始化完成后蜂鸣器响一声

def beep():
    GPIO.output(BUZZER, False)
    time.sleep(0.1)
    GPIO.output(BUZZER, True)
    time.sleep(0.001)

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

#行进中左转*测试中
def left_running(speed):
    pwm_LPWM.ChangeDutyCycle(80-speed)
    pwm_RPWM.ChangeDutyCycle(80+speed)

#行进中右转*测试中
def right_running(speed):
    pwm_LPWM.ChangeDutyCycle(80+speed)
    pwm_RPWM.ChangeDutyCycle(80-speed)
#关机
def shutdown():
    GPIO.cleanup()

#结束


