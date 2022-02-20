





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
            self.rect.y -= self.speed
        if status == 2:
            self.rect.y += self.speed
        if status == 3:
            self.rect.x -= self.speed
        if status == 4:
            self.rect.x -= self.speed