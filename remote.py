#遥控程序 By Animuses
import CAR
import time
import keyboard as k

CAR.init()
while True:
    if k.is_pressed('w'):
        CAR.forward(80,0.001)
        print('Forward')
        continue
    elif k.is_pressed('s'):
        CAR.backward(80,0.001)
        print('Backward')
        continue
    elif k.is_pressed('a'):
        CAR.left_running(30,0.001)
        print('Left')
        continue
    elif k.is_pressed('d'):
        CAR.right_running(30,0.001)
        print('Right')
        continue
    elif k.is_pressed('space'):
        CAR.stop(0.01)
        print('You pressed space!')
        continue
    elif k.is_pressed('q'):
        print('Quit!')
        break
