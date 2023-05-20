from pygame import *
from random import randint

once = False
left = False
right = False
up = False
down = False
win1 = False
win2 = False

point1 = 0
point2 = 0


class GameSprite(sprite.Sprite):
    def __init__(self, speed, pl_image, x, y, width, height):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(pl_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        self.list = []
        self.list.append(self)

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 700 - self.height:
            self.rect.y += self.speed


class Player2(GameSprite):
    global left, right, up, down

    def update(self):
        if up and self.rect.y > 0:
            self.rect.y -= self.speed
        if down and self.rect.y < 700 - self.height:
            self.rect.y += self.speed


class Ball(GameSprite):

    def update(self):
        global left, right, up, down, win1, win2, once
        global point1
        global point2

        if not once:
            up = False
            down = False
            right = False
            left = False
            er = randint(1, 2)
            er1 = randint(1, 2)
            if er == 1:
                left = True
            if er == 2:
                right = True
            if er1 == 1:
                up = True
            if er1 == 2:
                down = True
            once = True
        elif once:
            pass

        ##########################################
        if self.rect.x <= 0:
            win2 = True
        if self.rect.x >= 980:
            win1 = True
        if self.rect.y <= 0:
            up = False
            down = True
        if self.rect.y >= 700 - self.height:
            up = True
            down = False
        col1 = sprite.collide_rect(self, player1)
        col2 = sprite.collide_rect(self, player2)
        if col1:
            if up:
                if up:
                    up = False
                    down = True
                if down:
                    up = True
                    down = False
            left = False
            right = True

        if col2:
            if up:
                if up:
                    up = False
                    down = True
                if down:
                    up = True
                    down = False
            right = False
            left = True
        if self.rect.x <= 0 or self.rect.x >= 980:
            if left:
                point2 += 1
                self.rect.x = 480
                self.rect.y = 350
                once = False
            if right:
                point1 += 1
                self.rect.x = 480
                self.rect.y = 350
                once = False

        ##########################################
        if left:
            self.rect.x -= self.speed
        if right:
            self.rect.x += self.speed
        if up:
            self.rect.y -= self.speed
        if down:
            self.rect.y += self.speed


window = display.set_mode((980, 700))
display.set_caption('pingpong')
display.set_icon(image.load('мяч-transformed.png'))
window.fill((255, 255, 255))
font.init()
font1 = font.SysFont('TimesNewRoman', 100)
point12 = font1.render(str(point1), True, (0, 0, 0))
point21 = font1.render(str(point2), True, (0, 0, 0))
vs = font1.render(':', True, (0, 0, 0))
clock = time.Clock()
player1 = Player1(2, 'блок1-transformed.png', 100, 250, 20, 130)
player2 = Player2(1, 'блок2-transformed.png', 880, 250, 20, 130)
ball = Ball(1, 'мяч-transformed.png', 480, 350, 100, 99)

col1 = sprite.collide_rect(ball, player1)
col2 = sprite.collide_rect(ball, player2)

while True:

    point12 = font1.render(str(point1), True, (0, 0, 0))
    point21 = font1.render(str(point2), True, (0, 0, 0))
    window.fill((255, 255, 255))
    window.blit(point12, (350, 100))
    window.blit(point21, (550, 100))
    window.blit(vs, (450, 100))
    player1.reset()
    player2.reset()
    player1.update()
    player2.update()
    window.blit(point12, (350, 100))
    window.blit(point21, (550, 100))
    window.blit(vs, (450, 100))
    ball.reset()
    ball.update()

    for e in event.get():
        if e.type == QUIT:
            exit()
    clock.tick()

    display.update()
