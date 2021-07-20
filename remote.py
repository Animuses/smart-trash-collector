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
            if event.key == K_ESCAPE:
                print('Quit!')
                CAR.shutdown()
                pygame.quit()
                os._exit(0)
                break
                break
        if event.type == KEYUP:
            CAR.stop()
            
