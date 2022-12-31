import PySimpleGUI as sg
from time import time
from random import randint

def convert_pos_to_pixel(cell):
    tl = cell[0] * cell_size, cell[1] * cell_size
    br = tl[0] + cell_size, tl[1] + cell_size
    return tl, br

def place_apple():
    apple_pos = randint(0,cell_num - 1), randint(0,cell_num - 1)
    while apple_pos in snake_body:
        apple_pos = randint(0,cell_num - 1), randint(0,cell_num - 1)
    return apple_pos
field_size = 400
cell_num = 10
cell_size = field_size/cell_num

#snake_body
snake_body = [(4,4),(3,4),(2,4)]
directions = {'left': (-1,0), 'right': (1,0), 'up': (0,1), 'down':(0,-1)}
direction2 = directions['up']
# apple

apple_pos = place_apple()
apple_eaten = False

sg.theme('Green')
field = sg.Graph(
    canvas_size = (field_size,field_size),
    graph_bottom_left = (0,0),
    graph_top_right = (field_size,field_size),
    background_color = 'black'
)

layout = [[field]]

window = sg.Window('Snake', layout, return_keyboard_events = True)

start_time = time()
while True:
    event, values = window.read(timeout = 10)
    if event == sg.WIN_CLOSED:
        break


    if event == 'Left:37': direction2 = directions['left']
    if event == 'Up:38': direction2 = directions['up']
    if event == 'Right:39': direction2 = directions['right']
    if event == 'Down:40': direction2 = directions['down']

    tim_since_start = time() - start_time
    if tim_since_start >= 0.5:
        start_time = time()

        #apple snake collision
        if snake_body[0] == apple_pos:
            apple_pos = place_apple()
            apple_eaten = True

        #snake update
        new_head = (snake_body[0][0] + direction2[0],snake_body[0][1] + direction2[1])
        snake_body.insert(0, new_head)
        if not apple_eaten:
            snake_body.pop()
        apple_eaten = False

        #check death
        if not 0 <= snake_body[0][0] <= cell_size -1 or \
            not 0 <= snake_body[0][1] <= cell_num -1 or \
            snake_body[0] in snake_body[1:]:
            break

        field.DrawRectangle((0, 0), (field_size, field_size), 'black')

        tl, br = convert_pos_to_pixel(apple_pos)
        field.DrawRectangle(tl,br,'red')


        #field.DrawRectangle(topleft,bottomright,color)
        for index, part in enumerate(snake_body):
            tl, br = convert_pos_to_pixel(part)
            color = 'yellow' if index == 0 else 'green'
            field.DrawRectangle(tl,br,color)

window.close()