import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
import pygame

from player import Player
from shooting import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    game_clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    
    while True:
        screen.fill('black')
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        for obj in asteroids:
            if obj.is_colliding(player):
                print('Game over!')
                sys.exit(1)
        for obj in asteroids:
            for bullet in shots:
                if obj.is_colliding(bullet):
                    bullet.kill()
                    obj.split()
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
