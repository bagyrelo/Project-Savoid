from pyray import *
from raylib import *

class Player:
    def __init__(self, posx, posy, speedx, speedy, health, attack):
        self.posx = posx
        self.posy = posy
        self.speedx = speedx
        self.speedy = speedy
        self.health = health
        self.attack = attack
<<<<<<< HEAD
        self.texture = load_texture("assets/player.png")

    def draw(self):
        return draw_texture(self.texture, self.posx - self.texture.width // 2, self.posy - self.texture.height // 2, WHITE)
=======

    def draw(self):
        return draw_circle(self.posx, self.posy, 10, BLUE)
>>>>>>> 717cf33d719835ecbf1ac8daea3323620c112c4d
    
    def update(self):
        if is_key_down(KEY_W):
            self.posy -= self.speedy
        if is_key_down(KEY_S):
            self.posy += self.speedy
        if is_key_down(KEY_A):
            self.posx -= self.speedx
        if is_key_down(KEY_D):
            self.posx += self.speedx

    def attack(self, target):
        if check_collision_circles((self.posx, self.posy), 20, (target.posx, target.posy), 20):
            if is_key_down(KEY_SPACE):
                target.health -= self.attack
            
