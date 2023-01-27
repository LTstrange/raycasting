import math

import pygame
from pygame import Vector2
from pygame.color import THECOLORS

from ray import Ray


class Particle:
    def __init__(self, pos):
        self.fov = 60
        self.pos = Vector2(pos)
        self.heading = 0
        self.rays = [Ray(self.pos, rad) for rad in
                     range(int(self.heading - self.fov / 2), int(self.heading + self.fov / 2))]

    def draw(self, screen):
        for ray in self.rays:
            ray.draw(screen)

    def rotate(self, angle):
        self.heading += angle
        self.rays = [Ray(self.pos, rad) for rad in
                     range(int(self.heading - self.fov / 2), int(self.heading + self.fov / 2))]

    def move(self, ver, hor):
        d_pos = Vector2(ver, hor).normalize().rotate(self.heading)

        self.pos += d_pos * 2

    def look(self, walls):
        result = []
        for ray in self.rays:
            record = 849
            ray.length = 10
            ray.dir.normalize_ip()
            for wall in walls:
                point = ray.cast(wall)
                if point:
                    dist = ray.pos.distance_to(point)
                    if dist < record:
                        ray.dir.update(point - ray.pos)
                        ray.length = 1
                        record = dist
            else:
                a = ray.dir.as_polar()[1] - self.heading
                result.append(record * math.cos(a / 180 * math.pi))

        return result


if __name__ == '__main__':
    v1 = Vector2()
    v1.from_polar((1, -90))
    print(v1)
