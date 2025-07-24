import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    color_black = (0,0,0)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    Shot.containers = (shots,updatable,drawable)

    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable,)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color_black)

        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        for obj in asteroids:
            if obj.check_for_collision(player):
                print("Game over!")
                sys.exit()
        for obj in asteroids:
            for bullet in shots:
                if obj.check_for_collision(bullet):
                    obj.split()

        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
