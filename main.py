import pygame
import pygame_menu
from ball import Ball

pygame.init()
timer = pygame.time.Clock()

# 初始化屏幕
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 560
WHITE = (255, 255, 255)
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# 初始化菜单
title = "welcome"
MENU_WIDTH = 720
MENU_HEIGHT = 560
keep_running = True
menu = pygame_menu.Menu(title, MENU_WIDTH, MENU_HEIGHT, theme=pygame_menu.themes.THEME_BLUE)
is_menu_display = True

difficult = 5

timer = pygame.time.Clock()


# 开始游戏函数
def start_game():
    global is_menu_display
    is_menu_display = False


# 退出游戏函数
def stop_game():
    global keep_running
    keep_running = False


#难度更新
def change_diff(valus,difficulty):
    global difficult
    difficult = difficulty


# 添加菜单组件
menu.add.button("Play", start_game)
menu.add.selector("Diff:", [('easy', 8), ('normal', 16), ('hard', 24)], onchange=change_diff)
menu.add.button("Quit", stop_game)

ball = Ball()

while keep_running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            keep_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_menu_display = True
    if is_menu_display:
        menu.update(events)
        menu.draw(screen)
        ball.speedx = difficult
        ball.speedy = difficult
    else:
        screen.fill(WHITE)
        screen.blit(ball.img, (ball.x, ball.y))
        ball.sport()
        ball.touch_edge(SCREEN_WIDTH, SCREEN_HEIGHT)
    pygame.display.update()
    timer.tick(60)

pygame.quit()