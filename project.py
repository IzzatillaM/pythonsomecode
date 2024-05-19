import pygame

window = pygame.display.set_mode((700,500))
background = pygame.image.load('R (1).jpg')
background = pygame.transform.scale(background,(700, 500))

clock = pygame.time.Clock()
class GameSprite(pygame.sprite.Sprite):
    def __init__(self,player_image,x,y,width,height,speed):
        super().__init__()
        self.image = pygame.image.load(player_image)
        self.image = pygame.transform.scale(self.image,(width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def show(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Hero(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < 600:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
        if keys[pygame.K_SPACE]:
            self.fire()
    def fire(self):
        bullet = Bullet('laser_small.png', rocket.rect.centerx, rocket.top, 20, 30, 90)
        bullets.add(bullet)
rocket = Hero('img.png',250,400,100,100,10)

from random import randint
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.x = randint(0,600)
            self.rect.y = 0
bullets = pygame.sprite.Group()
monsters = pygame.sprite.Group()
for monster in range(5):
    monster = Enemy('enemy_1-removebg-preview (1).png',randint(0,700),50,40,50,randint(5,10))
    monsters.add(monster)
class Bullet(GameSprite):
    def update(self):

        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()


game = True
while game:
    window.blit(background, (0,0))
    rocket.show()
    rocket.update()
    monsters.draw(window)
    monsters.update()
    bullets.draw(window)
    bullets.update()
    events = pygame.event.get()
    for event in events:
     if event.type == pygame.QUIT:
          game = False

    pygame.display.update()
    clock.tick(60)




