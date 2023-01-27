import random

import pygame
from pygame.color import THECOLORS
from pygame.surface import Surface

from boundary import Boundary
from particle import Particle
from scene import Scene

width, height = 600, 600

pygame.init()
screen = pygame.display.set_mode((width * 2 + 4, height))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()

scene = Scene(602, 0, 600, 600)


def main():
    walls = [Boundary((random.uniform(0, width), random.uniform(0, height)),
                      (random.uniform(0, width), random.uniform(0, height))) for i in range(5)]
    walls.extend([Boundary((0, 0), (width-1, 0)),
                  Boundary((0, 0), (0, height-1)),
                  Boundary((width-1, height-1), (0, height-1)),
                  Boundary((width-1, 0), (width-1, height-1)),
                  ])
    paricle = Particle((100, 200))

    canvas = Surface((width, height)).convert_alpha()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_q]:
            paricle.rotate(-1)
        if pressed[pygame.K_e]:
            paricle.rotate(1)
        if pressed[pygame.K_w]:
            paricle.move(1, 0)
        if pressed[pygame.K_s]:
            paricle.move(-1, 0)
        if pressed[pygame.K_a]:
            paricle.move(0, -1)
        if pressed[pygame.K_d]:
            paricle.move(0, 1)


        scene.receive_vision(paricle.look(walls))
        scene.update()

        screen.fill(THECOLORS['black'])
        canvas.fill((0, 0, 0, 0))

        for wall in walls:
            wall.draw(screen)
        paricle.draw(canvas)

        Surface.blit(screen, canvas, screen_rect)
        Surface.blit(screen, scene.image, scene.rect)

        pygame.display.flip()


if __name__ == '__main__':
    main()
