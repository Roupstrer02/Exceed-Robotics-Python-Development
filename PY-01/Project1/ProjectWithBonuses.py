import pygame as pg
import random as rd
import time
pg.init()

size = (800,800)
screen = pg.display.set_mode(size)
clock = pg.time.Clock()

theme = "dark"
bgcolor = (0,0,0)
fgcolor = (255,255,255)

ball = pg.Rect(375,375,10,10)
playerPaddle = pg.Rect(50,350,25,100)
CPUPaddle = pg.Rect(725,350,25,100)

ballSpeedX = 5
ballSpeedY = 5
ballDirectionX = 1
ballDirectionY = 1
paddleSpeed = 8

playerScore = 0
CPUScore = 0
rally = 0
font = pg.font.Font('freesansbold.ttf', 32)



while True:
    #inputs
    pg.event.pump()
    mouseButtons = pg.mouse.get_pressed()

    #menu logic
    if mouseButtons[0]:
        break

    if mouseButtons[2]:
        if theme == "dark":
            theme = "light"
            bgcolor = (255,255,255)
            fgcolor = (0,0,0)
        elif theme == "light":
            theme = "dark"
            bgcolor = (0,0,0)
            fgcolor = (255,255,255)

    #updates
    startGameText = font.render("Left click to start game", True, fgcolor)
    closeGameText = font.render("Middle click during game to close", True, fgcolor)
    themeChangeText = font.render("Right click to change theme", True, fgcolor)

    #drawing
    screen.fill(bgcolor)
    #numbers found through trial and error
    screen.blit(startGameText, (222,300))
    screen.blit(closeGameText, (137,360))
    screen.blit(themeChangeText, (180,420))

    #clock
    pg.display.flip()

    if mouseButtons[2]:
        time.sleep(1)

    clock.tick(60)

while True:
    #inputs
    pg.event.pump()
    mousePos = pg.mouse.get_pos()
    mouseButtons = pg.mouse.get_pressed()

    #game logic
    if mouseButtons[1]:
        pg.quit()
        break

    if ball.y <= 0 or ball.y >= 790:
        ballDirectionY = -ballDirectionY

    if ball.x <= -10:
        CPUScore += 1
    if ball.x >= 800:
        playerScore += 1

    if ball.x <= -10 or ball.x >= 800:
        ball.x = 375
        ball.y = 375
        rally = 0
        CPUPaddle.y = 350

    if ball.colliderect(playerPaddle) or ball.colliderect(CPUPaddle):
        ballDirectionX = -ballDirectionX
        rally += 1
        if rd.random() > 0.5:
            ballDirectionY = -ballDirectionY


    #updates
    if CPUPaddle.center[1] < ball.center[1]:
        CPUPaddle.y += paddleSpeed
    elif CPUPaddle.center[1] > ball.center[1]:
        CPUPaddle.y -= paddleSpeed
    playerPaddle.y = mousePos[1] - 50

    totalSpeedX = ballSpeedX + rally
    totalSpeedY = ballSpeedY + rally
    ball.x += ballDirectionX * totalSpeedX
    ball.y += ballDirectionY * totalSpeedY
    playerScoreText = font.render("Player: " + str(playerScore), True, fgcolor)
    CPUScoreText = font.render("CPU: " + str(CPUScore), True, fgcolor)

    #drawing
    screen.fill(bgcolor)
    pg.draw.rect(screen, fgcolor, playerPaddle)
    pg.draw.rect(screen, fgcolor, ball)
    pg.draw.rect(screen, fgcolor, CPUPaddle)
    screen.blit(playerScoreText, (200,0))
    screen.blit(CPUScoreText, (500,0))

    #clock
    pg.display.flip()
    clock.tick(60)
