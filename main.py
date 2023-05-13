from pygame import *


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


window = display.set_mode((700, 500))
display.set_caption('pingpong')
display.set_icon(image.load('мяч-transformed.png'))
window.fill((255, 255, 255))

clock = time.Clock()
player1 = Player1(1, 'блок1-transformed.png', 100, 250, 20, 130)
player2 = Player2(1, 'блок2-transformed.png', 600, 250, 20, 130)

while True:

    window.fill((255, 255, 255))
    player1.reset()
    player2.reset()
    player1.update()
    player2.update()

    for e in event.get():
        if e.type == QUIT:
            exit()
    clock.tick()

    display.update()
