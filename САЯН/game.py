from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
# Создание окна
back = (99, 149, 194)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong by Yang')

# Переменные
FPS = 60
run = True
finish = False
clock = time.Clock()

# Создание мяча и ракетки
racket1 = Player('rocket1.png', 30, 200, 4, 50, 150)
racket2 = Player('rocket2.png', 520, 200, 4, 50, 150)
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)

font.init()
font1 = font.SysFont('Arial', 35)
lose1 = font1.render('ИГРОК ПЕРВЫЙ ПРОИГРАЛ!', True, (180, 0, 0))
lose2 = font1.render('ИГРОК ВТОРОЙ ПРОИГРАЛ!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if not finish:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        racket1.reset()
        racket2.reset()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
        
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

    display.update()
    clock.tick(FPS)