





import pygame


class Pad(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image_temp = pygame.image.load("./assets/pad/yellow.png")
        self.image = pygame.transform.scale(self.image_temp,(100,20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3

    def update(self, status):
        if status == 1:
            if self.rect.y >= 230:
               self.rect.y -= self.speed
        if status == 2:
            if self.rect.y <= 540:
                self.rect.y += self.speed
        if status == 3:
            if self.rect.x >= 0:
                self.rect.x -= self.speed
        if status == 4:
            if self.rect.x <= 700:
                self.rect.x -= self.speed