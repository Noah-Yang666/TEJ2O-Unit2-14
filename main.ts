/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Noah Yang
 * Created on: April 2026
 * This program moves a sprite clockwise and counter clockwise
*/

// variables needed
let sprite: game.LedSprite = null
let loopCounterX = 0
let loopCounterY = 0

// setting up
basic.clearScreen()
basic.showIcon(IconNames.Happy)

// pressing A, sprite moves clockwise
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    sprite = game.createSprite(0, 0)
    loopCounterX = 0
    loopCounterY = 0

    // moving sprite right
    while (loopCounterY <=4) {
        sprite.set(LedSpriteProperty.X, loopCounterY)
        loopCounterY +=1
        basic.pause(300)
    }

    // moving sprite down
    while (loopCounterX <= 4) {
        sprite.set(LedSpriteProperty.Y, loopCounterX)
        loopCounterX +=1
        basic.pause(300)
    }

    // moving sprite left
    while (loopCounterY >= 0) {
        sprite.set(LedSpriteProperty.X, loopCounterY)
        loopCounterY -=1
        basic.pause(300)
    }

    // moving sprite up
    while (loopCounterX >= 0) {
        sprite.set(LedSpriteProperty.Y, loopCounterX)
        loopCounterX -=1
        basic.pause(300)
    }

    // resetting
    sprite.delete()
    basic.clearScreen()
    basic.showIcon(IconNames.Happy)
})

// pressing B, sprite moves counter clockwise
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    sprite = game.createSprite(0, 0)
    loopCounterX = 0
    loopCounterY = 0

    // moving sprite down
    while (loopCounterX <= 4) {
        sprite.set(LedSpriteProperty.Y, loopCounterX)
        loopCounterX +=1
        basic.pause(300)
    }

    // moving sprite right
    while (loopCounterY <= 4) {
        sprite.set(LedSpriteProperty.X, loopCounterY)
        loopCounterY +=1
        basic.pause(300)
    }

    // moving sprite up
    while (loopCounterX >= 0) {
        sprite.set(LedSpriteProperty.Y, loopCounterX)
        loopCounterX -=1
        basic.pause(300)
    }

    // moving sprite left
    while (loopCounterY >= 0) {
        sprite.set(LedSpriteProperty.X, loopCounterY)
        loopCounterY -=1
        basic.pause(300)
    }

    // resetting
    sprite.delete()
    basic.clearScreen()
    basic.showIcon(IconNames.Happy)
})
