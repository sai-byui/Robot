# 1 - Import library
import pygame
from pygame.locals import *
import car

c = car.Car()

pygame.init()
width, height = 1280, 1000
screen=pygame.display.set_mode((width, height))
motion = 0 # -1 for backward, 1 for forward
direction = 0 # -50 for left, 50 for right, in between for lesser angles
playerpos=[100,100]


while 1:
    screen.fill(0)

    for event in pygame.event.get():
        # test events, set key states
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                motion = 1
            elif event.key == K_s:
                motion = -1
            elif event.key == K_a:
                direction = -50
            elif event.key == K_d:
                direction = 50
        elif event.type == pygame.KEYUP:
            if event.key == K_w or event.key == K_s:
                motion = 0
            elif event.key == K_a or event.key == K_d:
                direction = 0
    if motion == -1:
        c.backward(50)
    elif motion == 1:
        c.forward(50)

    c.turn(direction)