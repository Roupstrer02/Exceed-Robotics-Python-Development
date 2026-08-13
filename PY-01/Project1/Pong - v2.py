import pygame as pg
import random as rd
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((800,600))
clock = pg.time.Clock()

#colours
black = (0,0,0)
blue = (100,100,255)
red = (255,25,25)
green = (25,255,25)

#game objects
player1 = pg.Rect(50,250,25,150)
player2 = pg.Rect(725,250,25,150)
player2direction = 0
ball = pg.Rect(390,290,50,50)

#game object variables
ballXdirection = 1
ballYdirection = 1
ballspeed = 5
player2speed = 5

#score variables
player1score = 0
player2score = 0

#sound effect variables
hitsound = pg.mixer.Sound("hit.mp3")

#text variables
font = pg.font.Font(None, 80)

#images
bluePaddle = pg.image.load("BluePaddle.png")
redPaddle = pg.image.load("RedPaddle.png")
yellowBall = pg.image.load("Ball.png")

pg.mixer.music.load("music1.mp3")
pg.mixer.music.play()
while True:

    pg.event.pump()

    #inputs
    mousePos = pg.mouse.get_pos()

    #game logic
    if player2.y < ball.y - 40:
        player2direction = 1
    if player2.y > ball.y - 40:
        player2direction = -1

    if ball.y < 0:
        ballYdirection = 1
    if ball.y > 580:
        ballYdirection = -1

    if player2.colliderect(ball):
        ballXdirection = -1
        ballYdirection = rd.randint(-1,1)
        ballspeed += 1
        hitsound.play()

    if player1.colliderect(ball):
        ballXdirection = 1
        ballYdirection = rd.randint(-1,1)
        ballspeed += 1
        hitsound.play()
        
    if ball.x < -20:
        ball.x = 390
        ball.y = 290
        player2score += 1
        ballspeed = 5
        player2speed += 1
    if ball.x > 800:
        ball.x = 390
        ball.y = 290
        player1score += 1
        ballspeed = 5
        player2speed += 1

    #updates
    player1.y = mousePos[1] - 50
    player2.y += player2direction * player2speed
    ball.x += ballXdirection * ballspeed
    ball.y += ballYdirection * ballspeed
    player1scoretext = font.render(str(player1score), True, blue)
    player2scoretext = font.render(str(player2score), True, red)

    #drawing
    screen.fill(black)
    screen.blit(bluePaddle, (player1.x, player1.y))
    screen.blit(redPaddle, (player2.x - 25, player2.y))
    screen.blit(yellowBall, (ball.x, ball.y))
    screen.blit(player1scoretext, (200, 50))
    screen.blit(player2scoretext, (550, 50))

    #update frame
    pg.display.flip()
    clock.tick(60)

