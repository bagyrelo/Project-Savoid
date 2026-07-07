from pyray import *
from raylib import *
from player import *
from enemy import *

screen_width, screen_height = 800, 600

init_window(screen_width, screen_height, "Project Savoid")
set_target_fps(60)

ground = load_texture("Project-Savoid/assets/tux.png")

my_player = Player(get_screen_width() // 2, get_screen_height() // 2, 7, 7, 100, 5)
my_enemy = Skeleton(50, 10, 500, 200)

cam = Camera2D()
cam.target = (my_player.posx, my_player.posy)
cam.offset = (screen_width // 2, screen_height // 2)
cam.rotation = 0
cam.zoom = 1

while not window_should_close():
    cam.target = (my_player.posx, my_player.posy)
    cam.offset = (screen_width // 2, screen_height // 2)

    # Events

    if check_collision_circles((my_player.posx, my_player.posy), 15, (my_enemy.posx, my_enemy.posy), 15):
        my_enemy.update_attack(my_player, get_frame_time())
    else:
        my_enemy.attack_timer = 3.0

    # Update

    my_player.update()

    # Drawing
    begin_drawing()
    clear_background(BLACK)

    begin_mode_2d(cam)

    draw_texture(ground, screen_width//2 - ground.width//2, screen_height//2 - ground.height//2, WHITE)
    draw_text(TextFormat(b'%i', ffi.cast("int", my_player.health)), my_player.posx - 300, my_player.posy - 200, 30, BLUE)


    my_player.draw()
    my_enemy.draw()

    end_mode_2d()
    end_drawing()

unload_texture(ground)
close_window()
