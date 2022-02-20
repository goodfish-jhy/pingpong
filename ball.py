import pygame


class Ball():
    def __init__(self):
        self.img = img = pygame.image.load(".//assets//ball//blue.png")
        self.img = pygame.transform.scale(img, (40, 40))
        self.x = 40
        self.y = 40
        self.speedx = 5
        self.speedy = 5

    def sport(self):
        self.x += self.speedx
        self.y += self.speedy

    def touch_edge(self, width, height):
        if self.x > width - 40 or self.x < 0:
            self.speedx *= -1
        if self.y > height - 40 or self.y < 0:
            self.speedy *= -1
