import pygame

rect_size = 20
rect_mode = "[s] - Med"
speed_mode = '[q] - Fast'
screen_width = 1280
screen_height = 720
cur_row = 0
cur_col = 0
game_speed = 10
color = (255, 255, 255)
grid_on = True
grid_mode = '[g] - ON'

help_txt = ["There are two modes and a help screen.",
             "In edit mode use the arrow keys to control the red cursor and space to add or remove 'live' cells",
            "In run mode sit back and watch your creation. The speed of the sim may be changed during both edit & run modes.",
            "Special Keys:","[h] - Open and closes help menu", "[esc] - Switches between edit and run mode",
            "[space] - Adds or removes cells in edit mode", "[del] - Clears all live cells in edit mode",
            "[s] - Changes the size of cells", "[c] - Changes the color of cells", "[q] - Changes game speed",
            "[g] - Toggles Grid lines. Note: Gridlines on small and fine may cause performance issues", "Created by Kyle Moore - 3/28/23"]

intro_txt = "Welcome to Conway's game of Life!"
live_counter = 0

num_columns = screen_width // rect_size
num_rows = screen_height // rect_size

life_tracker = []
cursor_pos = [cur_row][cur_col]

x = 0
y = 0
mode = 'help'

up_arrow_pressed = False
down_arrow_pressed = False
right_arrow_pressed = False
left_arrow_pressed = False
esc_pressed = False
space_pressed = False
del_pressed = False
s_pressed = False # Game size
c_pressed = False # Cell color
q_pressed = False # Game Speed
h_presed = False # Help Menu
g_pressed = False # Grid Lines


def wipe():
    life_tracker.clear()
    for _ in range(int(num_rows)):
        life_tracker.append([0] * num_columns)

wipe()

def update_life_tracker(life_tracker, life_tracker_copy):
    new_life_tracker = []
    for row in range(num_rows):
        new_row = []
        for col in range(num_columns):
            live_counter = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    neighbor_row = row + i
                    neighbor_col = col + j
                    if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_columns:
                        if life_tracker_copy[neighbor_row][neighbor_col] == 1:
                            live_counter += 1

            if life_tracker_copy[row][col] == 1 and (live_counter < 2 or live_counter > 3):
                new_row.append(0)
            elif life_tracker_copy[row][col] == 0 and live_counter == 3:
                new_row.append(1)
            else:
                new_row.append(life_tracker_copy[row][col])

        new_life_tracker.append(new_row)
    return new_life_tracker




pygame.init()

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Conway")

run = 1
while run:
    if mode == 'run':
        pygame.time.delay(game_speed)
    else:
        pygame.time.delay(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False        
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                g_pressed = True
                if grid_on:
                    grid_on = False
                    grid_mode = "[g] - OFF"
                else:
                    grid_on = True
                    grid_mode = "[g] - ON"
            
            if event.key == pygame.K_c:
                c_pressed = True
                if color == (255, 255, 255):
                    color = (255, 255, 0)
                elif color == (255, 255, 0):
                    color = (255, 0, 0)
                elif color == (255, 0, 0):
                    color = (0, 0, 255)
                elif color == (0, 0, 255):
                    color = (0, 255, 0)
                elif color == (0, 255, 0):
                    color = (255, 0, 0)
                elif color == (255, 0, 0):
                    color = (0, 255, 255)
                elif color == (0, 255, 255):
                    color = (255, 255, 255)
                
            
            if event.key == pygame.K_q:
                q_pressed = True
                if game_speed == 0:
                    game_speed = 10
                    speed_mode = '[q] - Fast'
                elif game_speed == 10:
                    game_speed = 25
                    speed_mode = '[q] - Med'
                elif game_speed == 25:
                    game_speed = 75
                    speed_mode = '[q] - Slow'
                elif game_speed == 75:
                    game_speed = 150
                    speed_mode = '[q] - Turtle'
                elif game_speed == 150:
                    game_speed = 0
                    speed_mode = '[q] - Ludicrous'
            
            if event.key == pygame.K_h and not mode == 'run':
                h_presed = True
                if not mode == 'help':
                    mode = 'help'
                else:
                    mode = 'edit'
            
            if event.key == pygame.K_s and mode == 'edit' and not mode == 'help':
                s_pressed = True
                if rect_size == 5:
                    cur_col = 0
                    cur_row = 0
                    x = 0
                    y = 0
                    rect_size = 10
                    rect_mode = "[s] - Sml"
                    num_columns = screen_width // rect_size
                    num_rows = screen_height // rect_size
                    
                    wipe()
                    
                elif rect_size == 10 and mode == 'edit':
                    cur_col = 0
                    cur_row = 0
                    x = 0
                    y = 0
                    rect_size = 20
                    rect_mode = "[s] - Med"
                    num_columns = screen_width // rect_size
                    num_rows = screen_height // rect_size
                    wipe()
                    
                elif rect_size == 20 and mode == 'edit':
                    cur_col = 0
                    cur_row = 0
                    x = 0
                    y = 0
                    rect_size = 40
                    rect_mode = "[s] - Lg"
                    num_columns = screen_width // rect_size
                    num_rows = screen_height // rect_size
                    wipe()
                    
                elif rect_size == 40 and mode == 'edit':
                    cur_col = 0
                    cur_row = 0
                    x = 0
                    y = 0
                    rect_size = 5
                    rect_mode = "[s] - Fine"
                    num_columns = screen_width // rect_size
                    num_rows = screen_height // rect_size
                    wipe()
                    
                
            if event.key == pygame.K_DELETE and not del_pressed and mode == 'edit' and not mode == 'help':
                del_pressed = True
                wipe()
                

            if event.key == pygame.K_SPACE and not space_pressed and mode == 'edit' and not mode == 'help':
                space_pressed = True
                if life_tracker[cur_col][cur_row] == 1:
                    life_tracker[cur_col][cur_row] = 0
                elif life_tracker[cur_col][cur_row] == 0:
                    life_tracker[cur_col][cur_row] = 1
            
            if event.key == pygame.K_UP and not up_arrow_pressed and mode == 'edit' and not mode == 'help':
                up_arrow_pressed = True
                if y > 0:
                    y -= rect_size
                    cur_col -= 1
                    
            if event.key == pygame.K_DOWN and not down_arrow_pressed and mode == 'edit' and not mode == 'help':
                down_arrow_pressed = True
                if y < 720 - rect_size:
                    y += rect_size
                    cur_col += 1
                
            if event.key == pygame.K_RIGHT and not right_arrow_pressed and mode == 'edit' and not mode == 'help':
                right_arrow_pressed = True
                if x < 1280 - rect_size:
                    x += rect_size
                    cur_row += 1
                    
            if event.key == pygame.K_LEFT and not left_arrow_pressed and mode == 'edit' and not mode == 'help':
                left_arrow_pressed = True
                if x > 0:
                    x -= rect_size
                    cur_row -= 1
            
            if event.key == pygame.K_ESCAPE and not esc_pressed:
                esc_pressed = True
                if mode == 'edit':
                    mode = 'run'
                else:
                    mode = 'edit'
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up_arrow_pressed = False
            if event.key == pygame.K_DOWN:
                down_arrow_pressed = False
            if event.key == pygame.K_RIGHT:
                right_arrow_pressed = False
            if event.key == pygame.K_LEFT:
                left_arrow_pressed = False
            if event.key == pygame.K_ESCAPE:
                esc_pressed = False
            if event.key == pygame.K_SPACE:
                space_pressed = False
            if event.key == pygame.K_DELETE:
                del_pressed = False
            if event.key == pygame.K_h:
                h_pressed = False
            if event.key == pygame.K_c:
                c_pressed = False
            if event.key == pygame.K_g:
                g_pressed = False
                
    keys = pygame.key.get_pressed()

    win.fill((0, 0, 0))
    
    # Draws Cursor
    if mode == 'edit' and not mode == 'help':
        cursor_on = 255
    else:
        cursor_on = 0
    
    pygame.draw.rect(win, (cursor_on, 0, 0), (x, y, rect_size, rect_size))


    # Text
    font = pygame.font.SysFont(None, 30)
    font1 = pygame.font.SysFont(None, 15)
    title_font = pygame.font.SysFont(None, 45)
    
    size = font1.render(rect_mode, True, (255, 255, 255))
    speed = font1.render(speed_mode, True, (255, 255, 255))
    grid = font1.render(grid_mode, True, (255, 255, 255))
    
    
    if mode == 'help':
        intro = title_font.render(intro_txt, True, (0, 255, 255))
        win.blit(intro, ((1280/2 - 200) - 50, 15))
        for text in range(len(help_txt)):
            help = font.render(help_txt[text], True, (0, 255, 0))
            win.blit(help, (60, 60 + (22*text)))
            
    if not mode == 'help':
        win.blit(size, (10, 710))
        win.blit(speed, (70, 710))
        win.blit(grid, (150, 710))
        

    # Draws and updates the screen
    if not mode == 'help':
        for row in range(num_rows):
            for col in range(num_columns):
                if life_tracker[row][col]:
                    pygame.draw.rect(win, color, (col * rect_size, row * rect_size, rect_size, rect_size))
                if mode == 'edit' and grid_on:
                    pygame.draw.line(win, (127, 127, 127), (-10, row*rect_size), (1290, row*rect_size))
                    pygame.draw.line(win, (127, 127, 127), (col*rect_size, -10), (col*rect_size, 730))

    if not mode == help:
        if life_tracker and mode == 'run':
            life_tracker_copy = [row.copy() for row in life_tracker]
            life_tracker = update_life_tracker(life_tracker, life_tracker_copy)

    pygame.display.flip()

pygame.quit()