#遥控程序 By Animuses
import CAR
import time
import pygame
from pygame.locals import *
import os

CAR.init()
pygame.init()
size = width, hight = 100,100
screen = pygame.display.set_mode(size)
while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                CAR.forward(80)
                print('Forward')
            if event.key == K_DOWN:
                CAR.backward(80)
                print('Backward')
            if event.key == K_LEFT:
                CAR.left_spin(80)
                print('Left')
            if event.key == K_RIGHT:
                CAR.right_spin(80)
                print('Right')
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
            
