from pyray import *
from raylib import *

class Skeleton:
    def __init__(self, health, atack, x, y):
        self.health = health
        self.atack = atack
        self.x = x
        self.y = y
        self.last_attack_time = 0.0
        self.is_attacking = False
        self.cooldown = 3

    def hit(self, target):
        target.health -= self.atack
        wait_time(2.0)

    def draw(self):
        return draw_circle(self.x, self.y, 10, RED)
    
    def update(self, player):
        current_time = GetTime()
