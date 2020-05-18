import pygame
import time
pygame.init()

yellow=[255,255,0]
white=[255,255,255]
red=[255,0,0]

diswidth=800
disheight=800
dis=pygame.display.set_mode((diswidth,disheight))

pygame.display.set_caption("The Snake game")

clock=pygame.time.Clock()
snakespeed=30
snakeblock=10

game_over = False

x1=diswidth/2
y1=disheight/2
x1_change=0
y1_change=0

while not game_over:
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
            game_over=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x1_change=-10
                y1_change=0
            elif event.key==pygame.K_RIGHT:
                x1_change=10
                y1_change=0
            elif event.key==pygame.K_UP:
                x1_change=0
                y1_change=-10
            elif event.key==pygame.K_DOWN:
                x1_change=0
                y1_change=10

    if x1>=diswidth or x1<0 or y1>=disheight or y1<0:
        game_over=True

    x1 += x1_change
    y1 += y1_change

    dis.fill(yellow)

    pygame.draw.rect(dis,white,[x1,y1,snakeblock,snakeblock])
    pygame.display.update()

    clock.tick(snakespeed)

msg="You Lost"
font_style = pygame.font.SysFont(None, 50)
message = font_style.render(msg, True, red)
dis.blit(message, [diswidth/2, disheight/2])
pygame.display.update()

time.sleep(2)
pygame.quit()
quit()