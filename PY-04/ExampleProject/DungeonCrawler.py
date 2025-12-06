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

class Room:
    def __init__(self, roomtype, rx, ry, px, py):
        dx = 1000*rx - px + 500
        dy = 1000*ry - py + 500
        if roomtype == "standard":
            self.tiles = [pg.Rect(dx + 100, dy + 100, 800, 800),
            pg.Rect(dx + 900, dy + 450,100,100),
            pg.Rect(dx + 450, dy + 900,100,100)]

            if rx > 0:
                self.tiles.append(pg.Rect(dx + 0, dy + 450,100,100))
            if ry > 0:
                self.tiles.append(pg.Rect(dx + 450, dy + 0,100,100))
    def draw(self):
        for tile in self.tiles:
            pg.draw.rect(screen, "brown", tile)


def moveCamera(d, x, y):
    for row in d:
        for room in row:
            if room is not None:
                for tile in room.tiles:
                    tile.x += x
                    tile.y += y

def updateDungeon(d, p, x, y):
    if y > len(d)-1:
        #d.append([None for x in range(len(d), y-1)])
        d.append([Room("standard", x, y, p.position_x, p.position_y)])
    elif x > len(d[y])-1:
        for i in range(len(d[y]), x):
            d[y].append(None)
        d[y].append(Room("standard", x, y, p.position_x, p.position_y))
    elif d[y][x] is None:
        d[y][x] = Room("standard", x, y, p.position_x, p.position_y)



p = player()
dungeon = [[Room("standard", 0, 0, p.position_x, p.position_y)]]
enemies = []
while True:
    pg.event.pump()
    roomBefore = (p.room_x, p.room_y)
    cx, cy = p.control()
    roomAfter = (p.room_x, p.room_y)
    moveCamera(dungeon, cx, cy)
    if roomBefore != roomAfter:
        updateDungeon(dungeon, p, p.room_x, p.room_y)
        for r in dungeon:
            print(r)
        print('\n\n')




    screen.fill('black')
    for row in dungeon:
        for room in row:
            if room is not None:
                room.draw()
    p.draw()
    clock.tick(60)
    pg.display.flip()

















