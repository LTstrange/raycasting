import pygame
from pygame.color import THECOLORS
from pygame import Vector2


class Ray:
    def __init__(self, pos, rad):
        self.pos = pos
        self.dir = Vector2()
        self.dir.from_polar((1, rad))
        self.length = 10

    def draw(self, screen):
        pygame.draw.line(screen, (255, 255, 255, 100), self.pos, self.pos + self.dir * self.length)

    def look_at(self, mouse_pos):
        self.dir = mouse_pos - self.pos
        self.dir.normalize_ip()

    def cast(self, wall):
        x1, y1 = wall.a[0], wall.a[1]
        x2, y2 = wall.b[0], wall.b[1]

        x3, y3 = self.pos[0], self.pos[1]
        x4, y4 = x3 + self.dir[0], y3 + self.dir[1]

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0:
            return None

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

        if 0 < t < 1 and u > 0:
            x = x1 + t * (x2 - x1)
            y = y1 + t * (y2 - y1)
            return Vector2(x, y)
        else:
            return None
