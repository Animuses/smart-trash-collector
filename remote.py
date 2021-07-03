#/usr/bin/python3
#遥控程序 By Animuses
import CAR
from CAR import *
import time
import pygame
from pygame.locals import *
import os

CAR.init()
pygame.init()
size = width, hight = 100,100
screen = pygame.display.set_mode(size)
speed = 80
turn_speed = 80
HBHangle_now = 7.5
HBVangle_now = 7.5
HBJangle_now = 7.5
HHRangle_now = 7.5
HHangle_now = 7.5
while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_w:
                CAR.forward(speed)
                print('Forward')
            if event.key == K_s:
                CAR.backward(speed)
                print('Backward')
            if event.key == K_a:
                CAR.left_spin(speed)
                print('Left')
            if event.key == K_d:
                CAR.right_spin(speed)
                print('Right')
            if event.key == K_UP:
                CAR.Servo_pos(pwm_H_BASEV,HBVangle_now)
                print('HBUP')
            if event.key == K_DOWN:
                CAR.Servo_neg(pwm_H_BASEV,HBVangle_now)
                print('HBDOWN')
            if event.key == K_LEFT:
                CAR.Servo_pos(pwm_H_BASEH,HBVangle_now)
                print('HBLEFT')
            if event.key == K_RIGHT:
                CAR.Servo_neg(pwm_H_BASEH,HBVangle_now)
                print('HBRIGHT')
            if event.key == K_r:
                CAR.Servo_pos(pwm_H_JOINT,HBVangle_now)
                print('HJUP')
            if event.key == K_f:
                CAR.Servo_neg(pwm_H_JOINT,HBVangle_now)
                print('HJDOWN')
            if event.key == K_g:
                CAR.Servo_pos(pwm_H_HANDR,HBVangle_now)
                print('HHLEFT')
            if event.key == K_h:
                CAR.Servo_neg(pwm_H_HANDR,HBVangle_now)
                print('HHRIGHT')
            if event.key == K_v:
                CAR.Servo_pos(pwm_H_HAND,HBVangle_now)
                print('HHOPEN')
            if event.key == K_b:
                CAR.Servo_neg(pwm_H_HAND,HBVangle_now)
                print('HHCLOSE')
            if event.key == K_ESCAPE:
                print('Quit!')
                CAR.beep()
                CAR.shutdown()
                pygame.quit()
                os._exit(0)
                break
                break
        if event.type == KEYUP:
            CAR.stop()
            
