from pygame import *
from random import randint

once = False
win1 = False
win2 = False
up = False
down = False
right = False
left = False


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

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - self.height:
            self.rect.y += self.speed


class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_u] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_j] and self.rect.y < 500 - self.height:
            self.rect.y += self.speed


class Ball(GameSprite):

    def update(self):
        global win1, right, left, down, up
        global win2
        global once

        if not once:

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
            print(er, er1)
            once = True
        elif once:
            pass

        ##########################################
        if self.rect.x <= 0:
            win2 = True
        if self.rect.x >= 700:
            win1 = True
        if self.rect.y <= 0:
            print(6)
            up = False
            down = True

        if self.rect.y >= 700:
            print('5')
            up = True
            down = False
        col1 = sprite.collide_rect(self, player1)
        col2 = sprite.collide_rect(self, player2)
        if col1:
            if up:
                up = False
                down = True
            if down:
                up = True
                down = False
            if left:
                left = False
                right = True
            if right:
                left = True
                right = False

        if col2:
            if up:
                up = False
                down = True
            if down:
                up = True
                down = False
            if left:
                left = False
                right = True
            if right:
                left = True
                right = False

        ##########################################
        if left:
            self.rect.x -= self.speed
        if right:
            self.rect.x += self.speed
        if up:
            self.rect.y -= self.speed
        if down:
            self.rect.y += self.speed


window = display.set_mode((700, 500))
display.set_caption('pingpong')
display.set_icon(image.load('мяч-transformed.png'))
window.fill((255, 255, 255))

clock = time.Clock()
player1 = Player1(2, 'блок1-transformed.png', 100, 250, 20, 130)
player2 = Player2(2, 'блок2-transformed.png', 600, 250, 20, 130)
ball = Ball(1, 'мяч-transformed.png', 350, 250, 50, 49)

while True:

    window.fill((255, 255, 255))
    player1.reset()
    player2.reset()
    ball.reset()
    player1.update()
    player2.update()
    ball.update()
    for e in event.get():
        if e.type == QUIT:
            exit()
    clock.tick()

    display.update()
