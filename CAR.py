#!/usr/bin/python
#通用调用库 By Animuses
import RPi.GPIO as GPIO
import time

#初始化，设定引脚状态
def  init():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    global LIN1,LIN2,RIN1,RIN2,LPWM,RPWM,BUZZER,pwm_LPWM,pwm_RPWM
    LIN1 = 22
    LIN2 = 27
    LPWM = 18
    RIN1 = 25
    RIN2 = 24
    RPWM = 23
    BUZZER = 8
    GPIO.setup(LPWM,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(LIN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(LIN2,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(RPWM,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(RIN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(RIN2,GPIO.OUT,initial=GPIO.LOW)
    pwm_LPWM = GPIO.PWM(LPWM,2000)
    pwm_RPWM = GPIO.PWM(RPWM,2000)
    pwm_LPWM.start(0)
    pwm_RPWM.start(0)
    #初始化完成后蜂鸣器响一声*此处有待修改
    GPIO.output(BUZZER, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(BUZZER, GPIO.HIGH)
    time.sleep(0.001)

#停车
def stop(time):
    GPIO.output(LIN1, GPIO.LOW)
    GPIO.output(LIN2, GPIO.LOW)
    GPIO.output(RIN1, GPIO.LOW)
    GPIO.output(RIN2, GPIO.LOW)
    time.sleep(time)

#前进
def forward(speed,time):
    pwm_LPWM.ChangeDutyCycle(speed)
    pwm_RPWM.ChangeDutyCycle(speed)
    GPIO.output(LIN1, GPIO.HIGH)
    GPIO.output(LIN2, GPIO.LOW)
    GPIO.output(RIN1, GPIO.HIGH)
    GPIO.output(RIN2, GPIO.LOW)
    time.sleep(time)

#后退
def backward(speed,time):
    pwm_LPWM.ChangeDutyCycle(speed)
    pwm_RPWM.ChangeDutyCycle(speed)
    GPIO.output(LIN1, GPIO.LOW)
    GPIO.output(LIN2, GPIO.HIGH)
    GPIO.output(RIN1, GPIO.LOW)
    GPIO.output(RIN2, GPIO.HIGH)
    time.sleep(time)

#原地左转
def left_spin(speed,time):
    pwm_LPWM.ChangeDutyCycle(speed)
    pwm_RPWM.ChangeDutyCycle(speed)
    GPIO.output(LIN1, GPIO.HIGH)
    GPIO.output(LIN2, GPIO.LOW)
    GPIO.output(RIN1, GPIO.LOW)
    GPIO.output(RIN2, GPIO.HIGH)
    time.sleep(time)

#原地右转
def right_spin(speed,time):
    pwm_LPWM.ChangeDutyCycle(speed)
    pwm_RPWM.ChangeDutyCycle(speed)
    GPIO.output(LIN1, GPIO.LOW)
    GPIO.output(LIN2, GPIO.HIGH)
    GPIO.output(RIN1, GPIO.HIGH)
    GPIO.output(RIN2, GPIO.LOW)
    time.sleep(time)

#行进中左转*测试中
def left_running(speed,time):
    pwm_LPWM.ChangeDutyCycle(80-speed)
    pwm_RPWM.ChangeDutyCycle(80+speed)
    time.sleep(time)

#行进中右转*测试中
def right_running(speed,time):
    pwm_LPWM.ChangeDutyCycle(80+speed)
    pwm_RPWM.ChangeDutyCycle(80-speed)
    time.sleep(time)
#关机
def shutdown():
    GPIO.cleanup()

#结束


