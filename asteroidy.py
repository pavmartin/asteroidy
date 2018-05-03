#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:26:10 2018

@author: pav35118
"""

import pyglet
from pyglet.window.key import MOD_CTRL, A, B, C

window = pyglet.window.Window()

obrazek = pyglet.image.load('pig.png')
obrazek.anchor_x = obrazek.width // 2
obrazek.anchor_y = obrazek.height // 2
sprite = pyglet.sprite.Sprite(obrazek)


def tiktak(t):
    sprite.x = sprite.x + 10*t
    sprite.y = sprite.y + 10*t


@window.event
def on_draw():
    window.clear()
    sprite.draw()
    

@window.event
def on_mouse_press(x, y, button, mod):
    if button == 1:
        sprite.x = x
        sprite.y = y
    elif button == 4:
        sprite. rotation +=10
    
@window.event
def on_key_press(sym, mod):
    if sym != A:
        print(sym, mod)


pyglet.clock.schedule_interval(tiktak, 1/10)
pyglet.app.run()
print('Hotovo!')