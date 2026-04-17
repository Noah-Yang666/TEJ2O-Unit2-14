"""
Created by: Noah Yang
Created on: April 2026
This module is a Micro:bit MicroPython program that moves sprite around microbit
"""

from microbit import *

# variables needed
loopCounterX = 0
loopCounterY = 0

# setting up
display.clear()
display.show(Image.HAPPY)
while True:

    # when A's pressed, the pixels move clockwise
    if button_a.was_pressed():

        # setup
        display.clear()
        loopCounterX = 0
        loopCounterY = 0

        # goes left to right
        while loopCounterX < 4:
            display.set_pixel(0 + loopCounterX, 0 + loopCounterY, 9)
            sleep(500)
            display.set_pixel(0 + loopCounterX, 0 + loopCounterY, 0)
            loopCounterX += 1

        # goes up to down
        while loopCounterY < 4:
            display.set_pixel(0 + loopCounterX, 0 + loopCounterY, 9)
            sleep(500)
            display.set_pixel(0 + loopCounterX, 0 + loopCounterY, 0)
            loopCounterY += 1

        # goes right to left
        while loopCounterX > 0:
            display.set_pixel(0 + loopCounterX, 0 + loopCounterY, 9)
            sleep(500)
            display.set_pixel(0 + loopCounterX, 0 + loopCounterY, 0)
            loopCounterX -= 1

        # goes down to up
        while loopCounterY >= 0:
            display.set_pixel(0 + loopCounterX, 0 + loopCounterY, 9)
            sleep(500)
            display.set_pixel(0 + loopCounterX, 0 + loopCounterY, 0)
            loopCounterY -= 1
        display.show(Image.HAPPY)

    # when B's pressed, the pixels move counter clock wise
    if button_b.was_pressed():

        # setup
        display.clear()
        loopCounterX = 0
        loopCounterY = 0

        #  goes up to down
        while loopCounterY < 4:
            display.set_pixel(0 + loopCounterX, 0 + loopCounterY, 9)
            sleep(500)
            display.set_pixel(0 + loopCounterX, 0 + loopCounterY, 0)
            loopCounterY = loopCounterY + 1

        #  goes left to right
        while loopCounterX < 4:
            display.set_pixel(0 + loopCounterX, 0 + loopCounterY, 9)
            sleep(500)
            display.set_pixel(0 + loopCounterX, 0 + loopCounterY, 0)
            loopCounterX = loopCounterX + 1

        #  goes down to up
        while loopCounterY > 0:
            display.set_pixel(0 + loopCounterX, 0 + loopCounterY, 9)
            sleep(500)
            display.set_pixel(0 + loopCounterX, 0 + loopCounterY, 0)
            loopCounterY = loopCounterY - 1

        # goes right to left
        while loopCounterX >= 0:
            display.set_pixel(0 + loopCounterX, 0 + loopCounterY, 9)
            sleep(500)
            display.set_pixel(0 + loopCounterX, 0 + loopCounterY, 0)
            loopCounterX = loopCounterX - 1
        display.show(Image.HAPPY)
