





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

    def update(self, key):
        if key == pygame.K_UP:
            self.rect.y -= self.speed
        if key == pygame.K_DOWN:
            self.rect.y += self.speed
        if key == pygame.K_LEFT:
            self.rect.x -= self.speed
        if key == pygame.K_RIGHT:
            self.rect.x += self.speed