from pyray import *
from raylib import *

class Player:
    def __init__(self, posx, posy, speedx, speedy, health, atack):
        self.posx = posx
        self.posy = posy
        self.speedx = speedx
        self.speedy = speedy
        self.health = health
        self.atack = atack

    def draw(self):
        return draw_circle(self.posx, self.posy, 10, WHITE)
    
    def update(self):
        if is_key_down(KEY_W):
            self.posy -= self.speedy
        if is_key_down(KEY_S):
            self.posy += self.speedy
        if is_key_down(KEY_A):
            self.posx -= self.speedx
        if is_key_down(KEY_D):
            self.posx += self.speedx