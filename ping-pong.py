from pygame import *

win = display.set_mode((600, 500))
display.set_caption('Ping-pong')
win.fill((255, 255, 255))

font.init()
font = font.Font(None, 35)
lose_1 = font.render('player 1 lose!', True, (100, 0, 0))
lose_2 = font.render('player 2 lose!', True, (100, 0, 0))

speed_x = 4
speed_y = 4

a = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size):
        super().__init__()
        self.image = transform.scale(image.load(player_image), size)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 550:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 550:
            self.rect.y += self.speed

myach = GameSprite("w.png", 250, 250, 6, (50, 50))
player1 = Player("w2.png", 50, 100, 10, (30, 150))
player2 = Player("w2.png", 550, 100, 10, (30, 150))

while a:
    for e in event.get():
        if e.type == QUIT:
            a = False
    if finish != True:
        win.fill((255, 255, 255))
        myach.rect.x += speed_x
        myach.rect.y += speed_y
        player1.reset()
        player1.update_l()
        player2.reset()
        player2.update_r()
        myach.reset()
    if myach.rect.y > 450 or myach.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(player1, myach) or sprite.collide_rect(player2, myach):
        speed_x *= -1
    if myach.rect.x > 550:
        finish = True
        win.blit(lose_2, (200, 200))
    if myach.rect.x < 0:
        finish = True
        win.blit(lose_1, (200, 200))
    display.update()
    time.delay(50)
