from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
action = 0

while True:
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    
    if action == 0:
        if x < 800 and y == 90:
            x = x + 2
            #if x == 400:
                #action = 1
        elif x == 800 and y < 600:
            y = y + 2
        elif x > 0 and y == 600:
            x = x - 2
        elif x == 0 and y > 0:
            y = y - 2
    
    #elif action == 1:
        #x = 400 + 400 * math.sin(400 * math.pi)
        #y = 90 + 90 * math.cos(300 * math.pi)
            

    delay(0.001)

close_canvas()
