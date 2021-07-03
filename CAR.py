#!/usr/bin/python3
#通用调用库 By Animuses
#
import RPi.GPIO as GPIO
import time


#定义变量设定引脚接口与pwm
LIN1 = 20
LIN2 = 21
LPWM = 16
RIN1 = 19
RIN2 = 26
RPWM = 13
BUZZER = 8
H_BASEH = 23
H_BASEV = 11
H_JOINT = 9
H_HANDR = 10
H_HAND = 25
pwm_LPWM = GPIO.PWM(LPWM,2000)
pwm_RPWM = GPIO.PWM(RPWM,2000)
pwm_LPWM.start(0)
pwm_RPWM.start(0)
pwm_H_BASEH = GPIO.PWM(H_BASEH,50)
pwm_H_BASEV = GPIO.PWM(H_BASEV,50)
pwm_H_JOINT = GPIO.PWM(H_JOINT,50)
pwm_H_HANDR = GPIO.PWM(H_HANDR,50)
pwm_H_HAND = GPIO.PWM(H_HAND,50)
pwm_H_BASEH.start(7.5)
pwm_H_BASEV.start(7.5)
pwm_H_JOINT.start(7.5)
pwm_H_HANDR.start(7.5)
pwm_H_HAND.start(7.5)
#初始化，设定引脚状态
#L为左轮，R为右轮，PWM为占空比，调速用，H为机械臂
def  init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    #初始化GPIO引脚和初始化PWM并复位
    GPIO.setup(LPWM,GPIO.OUT)
    GPIO.setup(LIN1,GPIO.OUT)
    GPIO.setup(LIN2,GPIO.OUT)
    GPIO.setup(RPWM,GPIO.OUT)
    GPIO.setup(RIN1,GPIO.OUT)
    GPIO.setup(RIN2,GPIO.OUT)
    GPIO.setup(BUZZER,GPIO.OUT)
    GPIO.setup(H_BASEH,GPIO.OUT)
    GPIO.setup(H_BASEV,GPIO.OUT)
    GPIO.setup(H_JOINT,GPIO.OUT)
    GPIO.setup(H_HANDR,GPIO.OUT)
    GPIO.setup(H_HAND,GPIO.OUT)
    beep()
    #初始化完成后蜂鸣器响一声

#初始化结束

#############
#通用部件部分#
#############

#蜂鸣器响一声
def beep():
    GPIO.output(BUZZER, False)
    time.sleep(0.1)
    GPIO.output(BUZZER, True)
    time.sleep(0.005)

#关机
def shutdown():
    GPIO.cleanup()


##############
##小车运动部分#
##############

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
    pwm_LPWM.ChangeDutyCycle(speed)
    pwm_RPWM.ChangeDutyCycle(speed)

#行进中右转*测试中
def right_running(speed):
    pwm_LPWM.ChangeDutyCycle(speed)
    pwm_RPWM.ChangeDutyCycle(speed)


##############
##舵机控制部分#
##############

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


#结束
