import pygame
import math

screen_x=1000
screen_y=530
screen = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("Pong game")
icon = pygame.image.load('ping-pong.png')
pygame.display.set_icon(icon)
background = pygame.image.load('pong background.png')

# player 1
playerimg=pygame.image.load('bar.png')
player_x=10
player_y=screen_y/2 - 64
player_dy=0
scoreplayer1=0

# player 2
player2img=pygame.image.load('bar.png')
player_2x=screen_x-(65*2)
player_2y=screen_y/2 - 64
player_2dy=0
scoreplayer2=0

# net
netimg = pygame.image.load('dashed-line (1).png')
net_x=screen_x/2 - 256
net_y=screen_y/2 - 256

# ball
ballimg = pygame.image.load('ball1.png')
ball_x= player_x + 72
ball_y = screen_y/2
ball_dx=5
ball_dy=5

def player1(x,y):
    screen.blit(playerimg,(x,y))

def player2(x,y):
    screen.blit(player2img,(x,y))

def net(x,y):
    screen.blit(netimg,(x,y))

def ball(x,y):
    screen.blit(ballimg,(x,y))

running = True

while running:
    screen.fill((0,0,0))
    #screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                player_dy=-6
            if event.key==pygame.K_s:
                player_dy=6
            if event.key==pygame.K_UP:
                player_2dy=-6
            if event.key==pygame.K_DOWN:
                player_2dy=6
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_w or event.key==pygame.K_s:
                player_dy=0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                player_2dy=0

    player_y+=player_dy
    player_2y+=player_2dy

    if player_y<0:
        player_y=0
    if player_y>=screen_y - 128:
        player_y=screen_y-128
    if player_2y<0:
        player_2y=0
    if player_2y>=screen_y - 128:
        player_2y=screen_y-128

    
   

    # detect collision with top and bottom walls
    if ball_y <= 0 or ball_y >= screen_y - 64:
       ball_dy = -ball_dy
    if ball_x == screen_x:
        scoreplayer1+=1
    if ball_x == 0:
        scoreplayer2+=1
    # detect collision with player 1's bar
    if ball_x <= player_x + 64 and ball_y >= player_y and ball_y <= player_y + 128:
        ball_dx = 5

    # detect collision with player 2's bar
    if ball_x >= player_2x + 64 and ball_y >= player_2y and ball_y <= player_2y + 128:
        ball_dx = -5
    
    ball_x +=ball_dx
    ball_y += ball_dy
    if scoreplayer2==10 or scoreplayer1==10:
        running = False
        print(scoreplayer1,scoreplayer2)
    ball(ball_x,ball_y)
    net(net_x,net_y)
    player1(player_x,player_y)
    player2(player_2x,player_2y)
    pygame.display.update()