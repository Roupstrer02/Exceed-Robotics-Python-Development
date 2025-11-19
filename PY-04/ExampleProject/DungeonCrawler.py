from pygame import Rect
import pygame as pg

pg.init()
screenSize = (1000,1000)
screen = pg.display.set_mode(screenSize)
clock = pg.time.Clock()

class player:
    hp = 10
    atk = 1
    armor = 0
    hitbox = Rect(475,475,50,50)

    up = pg.K_w
    down = pg.K_s
    left = pg.K_a
    right = pg.K_d
    speed = 5

    def control(self):
        keys = pg.key.get_pressed()

        if keys[self.up]:
            self.hitbox.y -= self.speed
        if keys[self.down]:
            self.hitbox.y += self.speed
        if keys[self.left]:
            self.hitbox.x -= self.speed
        if keys[self.right]:
            self.hitbox.x += self.speed

    def draw(self):
        pg.draw.rect(screen, 'lightblue', self.hitbox)

class room:
    tiles = []


p = player()
while True:
    pg.event.pump()

    p.control()





    screen.fill('black')
    p.draw()
    clock.tick(60)
    pg.display.flip()

















