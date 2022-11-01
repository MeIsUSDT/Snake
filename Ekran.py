import pygame
import time
import random
import keyboard

pygame.init()
green = (102, 255, 102)
black = (0, 0, 0)
red = (204, 0, 0)
pink = (255, 102, 178)

dis_height = 400
dis_width = 1000
snake_block = 10
step = 10
snake_speed = 500
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Zmiika')
bg = pygame.image.load("lol.jpeg")
game_over = False
x1 = round(dis_width/2) -200
y1 = round(dis_height/4)
x1_change = 0
y1_change = 0
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 100, italic = True)
def our_snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3, dis_height/3])  
def gameLoop():
    game_over  = False
    game_close = False
    x1 = dis_width/2
    y1 = dis_height/2
    x1_change = 0
    y1_change = 0
    foodx = round(random.randrange(0, dis_width - snake_block) /10) * 10
    foody = round(random.randrange(0, dis_height - snake_block) /10) * 10
    snake_List = []
    Lenth_of_snake = 1
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if keyboard.is_pressed('esc'):
                    game_over = True
        while game_close == True:
            dis.fill(black)
            message('To restart Press R;/n To Quit Press Q', pink)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = False
                        game_over = True
                    if event.key == pygame.K_r:
                        gameLoop()
                    if event.key == pygame.K_Q:
                        game_close = False
                        game_over = True
                    if event.key == pygame.K_R:
                        gameLoop()
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1<0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(black)
            dis.blit(bg, (0, 0))
            def create_food():
                pygame.draw.rect(dis, pink, [foodx, foody, snake_block, snake_block])
            create_food()
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Lenth_of_snake:
                del snake_List[0]
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True
            our_snake(snake_block, snake_List)
            pygame.display.update()
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) /10) * 10
                foody = round(random.randrange(0, dis_height - snake_block) /10) * 10
                print('Mmm...')
                Lenth_of_snake += 1
            clock.tick(snake_speed)
            pygame.display.update()
    message("YOU'RE DEAD", red)
    pygame.display.update()
    time.sleep(1)
    pygame.quit()
    quit()

gameLoop()
