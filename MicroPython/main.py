"""
Created by: Noah Yang
Created on: April 2026
This module is a Micro:bit MicroPython program that moves sprite around microbit
"""

from microbit import *

# variables needed
sprite = None
loopCounterX = 0
loopCounterY = 0

# setting up
display.clear()
display.show(Image.HAPPY)

# pressing A, sprite moves clockwise
while True:
    if button_a.was_pressed():
        display.clear()
        sprite = game.create_sprite(0, 0)
        loopCounterX = 0
        loopCounterY = 0

        # moving sprite right
        while loopCounterY <= 4:
            sprite.set_x(loopCounterY)
            loopCounterY += 1
            sleep(300)

        # moving sprite down
        while loopCounterX <= 4:
            sprite.set_y(loopCounterX)
            loopCounterX += 1
            sleep(300)

        # moving sprite left
        while loopCounterY >= 0:
            sprite.set_x(loopCounterY)
            loopCounterY -= 1
            sleep(300)

        # moving sprite up
        while loopCounterX >= 0:
            sprite.set_y(loopCounterX)
            loopCounterX -= 1
            sleep(300)

        # resetting
        sprite.delete()
        display.clear()
        display.show(Image.HAPPY)

    # pressing B, sprite moves counter clockwise
    if button_b.was_pressed():
        display.clear()
        sprite = game.create_sprite(0, 0)
        loopCounterX = 0
        loopCounterY = 0

        # moving sprite down
        while loopCounterX <= 4:
            sprite.set_y(loopCounterX)
            loopCounterX += 1
            sleep(300)

        # moving sprite right
        while loopCounterY <= 4:
            sprite.set_x(loopCounterY)
            loopCounterY += 1
            sleep(300)

        # moving sprite up
        while loopCounterX >= 0:
            sprite.set_y(loopCounterX)
            loopCounterX -= 1
            sleep(300)

        # moving sprite left
        while loopCounterY >= 0:
            sprite.set_x(loopCounterY)
            loopCounterY -= 1
            sleep(300)

        # resetting
        sprite.delete()
        display.clear()
        display.show(Image.HAPPY)
