#!/usr/bin/python3
#自动小车主程序 By Animuses

#导入模块并初始化
import CAR
from CAR import *
import time
import os

#初始化小车，完成响两声
CAR.init()
#等待0.05秒后开始执行操作
time.sleep(0.05)

#小车走固定路线移动，以下为各个指令的使用示例
#理论上一个动作可以不停下直接接下一个动作，实际情况有待实验
#有BUG再慢慢修吧

#指定速度为80前进
CAR.forward(80)
#前进1秒
time.sleep(1)

#停下
CAR.stop()
#停下1秒
time.sleep(1)

#指定速度为80后退
CAR.backward(80)
#后退1秒
time.sleep(1)

#停下
CAR.stop()
#停下1秒
time.sleep(1)

#指定速度为60原地左转
CAR.left_spin(60)
#左转0.5秒
time.sleep(0.5)

#停下
CAR.stop()
#停下1秒
time.sleep(1)

#指定速度为60原地右转
CAR.right_spin(60)
#右转0.5秒
time.sleep(0.5)

#停下
CAR.stop()
#停下1秒
time.sleep(1)

#打开扫帚
CAR.sweep_open()

#闭合扫帚
CAR.sweep_close()

#yolo识别电池
CAR.recognize(0)