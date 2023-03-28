import pygame

rect_size = 20
screen_width = 1280
screen_height = 720
cur_row = 0
cur_col = 0

num_columns = screen_width // rect_size
num_rows = screen_height // rect_size

life_tracker = []
cursor_pos = [cur_row][cur_col]


x = 0
y = 0
mode = 'edit'

up_arrow_pressed = False
down_arrow_pressed = False
right_arrow_pressed = False
left_arrow_pressed = False
esc_pressed = False
space_pressed = False
del_pressed = False
def wipe():
    for _ in range(num_rows):
        life_tracker.append([0] * num_columns)

wipe()

pygame.init()

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Conway")

run = 1
while run:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Cursor
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DELETE and not del_pressed and mode == 'edit':
                del_pressed = True
                wipe()
                
            
            if event.key == pygame.K_SPACE and not space_pressed and mode == 'edit':
                space_pressed = True
                if life_tracker[cur_col][cur_row] == 1:
                    life_tracker[cur_col][cur_row] = 0
                elif life_tracker[cur_col][cur_row] == 0:
                    life_tracker[cur_col][cur_row] = 1
            
            if event.key == pygame.K_UP and not up_arrow_pressed and mode == 'edit':
                up_arrow_pressed = True
                if y > 0:
                    y -= 20
                    cur_col -= 1
                    
            if event.key == pygame.K_DOWN and not down_arrow_pressed and mode == 'edit':
                down_arrow_pressed = True
                if y < 700:
                    y += 20
                    
                    cur_col += 1
                    
            if event.key == pygame.K_RIGHT and not right_arrow_pressed and mode == 'edit':
                right_arrow_pressed = True
                if x < 1260:
                    x += 20
                    cur_row += 1
            if event.key == pygame.K_LEFT and not left_arrow_pressed and mode == 'edit':
                left_arrow_pressed = True
                if x > 0:
                    x -= 20
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
                ctrl_pressed = False
                
                
    keys = pygame.key.get_pressed()

    win.fill((0, 0, 0))
    
    # Draws Cursor
    if mode == 'edit':
        cursor_on = 255
    else:
        cursor_on = 0
    
    pygame.draw.rect(win, (cursor_on, 0, 0), (x, y, 20, 20))



    # Draws and updates the screen
    for row in range(num_rows):
        for col in range(num_columns):
            if life_tracker[row][col]:
                pygame.draw.rect(win, (255, 255, 255), (col * rect_size, row * rect_size, rect_size, rect_size))
            


    pygame.display.flip()

pygame.quit()