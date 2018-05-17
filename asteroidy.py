#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:26:10 2018

@author: pav35118
"""

import pyglet
from pyglet.window.key import DOWN, UP, LEFT, RIGHT, MOD_CTRL, MOD_SHIFT
from pyglet.window.mouse import LEFT as mLEFT
from pyglet.window.mouse import RIGHT as mRIGHT
from math import sin, cos, pi

window = pyglet.window.Window()

obrazek = pyglet.image.load('obrazek.png')
obrazek.anchor_x = obrazek.width // 2
obrazek.anchor_y = obrazek.height // 2
sprite = pyglet.sprite.Sprite(obrazek)


uhel = sprite.rotation = 60
rychlost = 30
klavesy = set()


def tiktak(t):
    global rychlost
    global uhel

    # posun
    sprite.x = sprite.x + rychlost*t*sin(pi*uhel/180)
    sprite.y = sprite.y + rychlost*t*cos(pi*uhel/180)

    # natočení
    for sym in klavesy:
        if sym == DOWN:
            if rychlost < 10:
                rychlost = 0
            else:
                rychlost -= 10*t
        if sym == UP:
            if rychlost > 90:
                rychlost = 100
            rychlost += 10
        if sym == LEFT:
            uhel -= 10
            sprite.rotation -= 10
        if sym == RIGHT:
            uhel += 10
            sprite.rotation += 10


@window.event
def on_draw():
    window.clear()
    sprite.draw()


@window.event
def on_mouse_press(x, y, button, mod):
    global uhel
    if button == mLEFT:
        sprite.x = x
        sprite.y = y
    elif button == mRIGHT and (mod & MOD_SHIFT):
        sprite.rotation += 180
        uhel += 180
    elif button == mRIGHT and (mod & MOD_CTRL):
        sprite.rotation += 90
        uhel += 90
    elif button == mRIGHT:
        sprite.rotation += 10
        uhel += 10


@window.event
def on_key_press(sym, mod):
    global klavesy
    klavesy.add(sym)


@window.event
def on_key_release(sym, mod):
    global klavesy
    klavesy.remove(sym)




pyglet.clock.schedule_interval(tiktak, 1/25)

pyglet.app.run()
print('Hotovo!')