import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)

    def draw(self, screen):
        color_white = (255,255,255)
        pygame.draw.circle(screen,color_white,self.position,SHOT_RADIUS,2)
    def update(self,dt):
        self.position += (self.velocity * dt)