from pygame import Rect
import pygame as pg
from random import randint
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
    speed = 20
    room_x = 0
    room_y = 0
    position_x = 500
    position_y = 500


    def control(self):
        keys = pg.key.get_pressed()


        cam_x = 0
        cam_y = 0
        if keys[self.up]:
            cam_y += self.speed
        if keys[self.down]:
            cam_y -= self.speed
        if keys[self.left]:
            cam_x += self.speed
        if keys[self.right]:
            cam_x -= self.speed

        self.position_x -= cam_x
        self.position_y -= cam_y
        self.room_x = self.position_x // 1000
        self.room_y = self.position_y // 1000
        return cam_x, cam_y

    def draw(self):
        pg.draw.rect(screen, 'lightblue', self.hitbox)


class Enemy:
    hp = 10
    atk = 1
    armor = 0

    speed = 20

    def __init__(self, rx, ry, px, py):
        self.room_x = rx
        self.room_y = ry
        self.starting_x = px
        self.starting_y = py
        dx = 1000 * rx - px + 500
        dy = 1000 * ry - py + 500
        self.hitbox = Rect(dx, dy, 75, 75)

    def draw(self):
        pg.draw.ellipse(screen, 'red', self.hitbox)
        print(self.hitbox.x, self.hitbox.y)

class Room:
    enemies = []
    def __init__(self, roomtype, rx, ry, px, py):
        self.rt = roomtype
        self.rx = rx
        self.ry = ry
        dx = 1000 * rx - px + 500
        dy = 1000 * ry - py + 500
        self.tiles = [pg.Rect(dx + 100, dy + 100, 800, 800),
        pg.Rect(dx + 900, dy + 450,100,100),
        pg.Rect(dx + 450, dy + 900,100,100)]
        if rx > 0:
            self.tiles.append(pg.Rect(dx + 0, dy + 450,100,100))
        if ry > 0:
            self.tiles.append(pg.Rect(dx + 450, dy + 0,100,100))

        #roomtype specific walls & enemies
        if roomtype == "standard":
            pass
        elif roomtype == "danger":
            self.enemies.append(Enemy(rx, ry, 300, 300))
    def draw(self):
        if self.rt == "standard":
            for tile in self.tiles:
                pg.draw.rect(screen, "gray", tile)
        elif self.rt == "danger":
            for tile in self.tiles:
                pg.draw.rect(screen, "darkgreen", tile)

        for enemy in self.enemies:
            enemy.draw()





def moveCamera(d, x, y):
    for row in d:
        for room in row:
            if room is not None:
                for tile in room.tiles:
                    tile.x += x
                    tile.y += y
                for e in room.enemies:
                    e.hitbox.x += x
                    e.hitbox.y += y

def updateDungeon(d, rTypes, p, x, y):
    if y > len(d)-1:
        newrow = [None for X in range(0, x)]
        newrow.append(Room(rTypes[randint(0,len(rTypes)-1)], x, y, p.position_x, p.position_y))
        d.append(newrow)
    elif x > len(d[y])-1:
        for i in range(len(d[y]), x):
            d[y].append(None)
        d[y].append(Room(rTypes[randint(0,len(rTypes)-1)], x, y, p.position_x, p.position_y))
    elif d[y][x] is None:
        d[y][x] = Room(rTypes[randint(0,len(rTypes)-1)], x, y, p.position_x, p.position_y)



p = player()
dungeon = [[Room("standard", 0, 0, p.position_x, p.position_y)]]
roomTypes = ["standard", "danger"]

while True:
    pg.event.pump()
    roomBefore = (p.room_x, p.room_y)
    cx, cy = p.control()
    roomAfter = (p.room_x, p.room_y)
    moveCamera(dungeon, cx, cy)
    if roomBefore != roomAfter:
        updateDungeon(dungeon, roomTypes, p, p.room_x, p.room_y)





    screen.fill('black')
    for row in dungeon:
        for room in row:
            if room is not None:
                room.draw()
    p.draw()
    clock.tick(60)
    pg.display.flip()

















