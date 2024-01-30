from dataclasses import dataclass

from pygame import Surface, Color

import pygame

@dataclass
class Circle:
    center: tuple
    radius: int

    def render(self, surface: Surface, thickness: int, color: Color) -> None:
        x = 0
        y = self.radius
        m = 5 - 4 * self.radius
        
        while y >= x:
            surface.set_at((self.center[0] + x, self.center[1] + y), color)
            surface.set_at((self.center[0] + y, self.center[1] + x), color)
            surface.set_at((self.center[0] - x, self.center[1] + y), color)
            surface.set_at((self.center[0] - y, self.center[1] + x), color)

            surface.set_at((self.center[0] + x, self.center[1] - y), color)
            surface.set_at((self.center[0] + y, self.center[1] - x), color)
            surface.set_at((self.center[0] - x, self.center[1] - y), color)
            surface.set_at((self.center[0] - y, self.center[1] - x), color)

            if m > 0:
                y -= 1
                m -= 8 * y

            x += 1
            m += 8 * x + 4
