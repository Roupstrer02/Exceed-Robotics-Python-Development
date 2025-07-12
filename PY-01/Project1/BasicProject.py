import pygame as pg

pg.init()

size = (800,800)
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
black = (0,0,0)
white = (255,255,255)

ball = pg.Rect(375,375,10,10)
playerPaddle = pg.Rect(50,350,25,100)
CPUPaddle = pg.Rect(725,350,25,100)

ballSpeedX = 5
ballSpeedY = 5
paddleSpeed = 5

while True:
    #inputs
    pg.event.pump()
    mousePos = pg.mouse.get_pos()
    mouseButtons = pg.mouse.get_pressed()

    #game logic
    if mouseButtons[0]:
        break
    if CPUPaddle.y <= 0 or CPUPaddle.y >= 700:
        paddleSpeed = -paddleSpeed
    
    if ball.y <= 0 or ball.y >= 790:
        ballSpeedY = -ballSpeedY

    if ball.x <= -10 or ball.x >= 800:
        ball.x = 375
        ball.y = 375

    if ball.colliderect(playerPaddle) or ball.colliderect(CPUPaddle):
        ballSpeedX = -ballSpeedX

    #updates
    CPUPaddle.y += paddleSpeed
    playerPaddle.y = mousePos[1] - 50
    ball.x += ballSpeedX
    ball.y += ballSpeedY

    #drawing
    screen.fill(black)
    pg.draw.rect(screen, white, playerPaddle)
    pg.draw.rect(screen, white, ball)
    pg.draw.rect(screen, white, CPUPaddle)

    #clock
    pg.display.flip()
    clock.tick(60)