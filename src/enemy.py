from pyray import *
from raylib import *

delta_time = get_frame_time()

class Skeleton:
    def __init__(self, health, attack, posx, posy):
        self.health = health
        self.attack = attack
        self.posx = posx
        self.posy = posy
        self.attack_timer = 3.0
        self.cooldown = 3

    def hit(self, target):
        target.health -= self.attack

    def draw(self):
        return draw_circle(self.posx, self.posy, 10, RED)
    
    def update_attack(self, target, delta_time):
        self.attack_timer += delta_time

        if self.attack_timer >= self.cooldown:
            self.hit(target)
            self.attack_timer = 0
