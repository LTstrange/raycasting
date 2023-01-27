import math

import pygame
from pygame import Vector2, Surface
from pygame.color import THECOLORS
from pygame.rect import Rect


def color_map(origin, low, high, new_low, new_high):
    result = origin / (high - low) * (new_high - new_low) + new_low
    result = result if result > min(new_low, new_high) else min(new_low, new_high)
    result = result if result < max(new_low, new_high) else max(new_low, new_high)
    return result


def dist_map(origin, low, high, new_low, new_high):
    return origin / (high - low) * (new_high - new_low) + new_low


class Scene:
    def __init__(self, x, y, w, h):
        self.pos = Vector2(x, y)
        self.width = w
        self.height = h

        self.vision = []

        self.image = Surface((w, h)).convert_alpha()
        self.image.fill(THECOLORS['black'])
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def receive_vision(self, distences):
        self.vision = distences

    def update(self):
        self.image.fill(THECOLORS['black'])

        w = self.rect.width / len(self.vision)
        for index, dist in enumerate(self.vision):
            h = dist_map(dist, 0, 849, 400, 0)

            rect = Rect(index * w, 300 - h / 2, w + 1, h)
            pygame.draw.rect(self.image, (255, 255, 255, color_map(dist, 0, 600, 255, 0)), rect, 0)
