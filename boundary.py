import pygame
from pygame.color import THECOLORS
from pygame import Vector2


class Boundary:
    def __init__(self, posA, posB):
        self.a = Vector2(posA)
        self.b = Vector2(posB)

    def draw(self, screen):
        pygame.draw.line(screen, THECOLORS['white'], self.a, self.b)