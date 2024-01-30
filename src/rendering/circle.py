from dataclasses import dataclass

from pygame import Surface, Color

import pygame

@dataclass
class Circle:
    center: tuple
    radius: int

    def render_pixels(self, surface: Surface, x, y, color) -> None:
        surface.set_at((self.center[0] + x, self.center[1] + y), Color(255, 0, 0))
        surface.set_at((self.center[0] + y, self.center[1] + x), Color(255, 127, 0))
        surface.set_at((self.center[0] - x, self.center[1] + y), Color(255, 255, 0))
        surface.set_at((self.center[0] - y, self.center[1] + x), Color(255, 255, 127))

        surface.set_at((self.center[0] + x, self.center[1] - y), Color(255, 255, 255))
        surface.set_at((self.center[0] + y, self.center[1] - x), Color(127, 255, 255))
        surface.set_at((self.center[0] - x, self.center[1] - y), Color(0, 255, 255))
        surface.set_at((self.center[0] - y, self.center[1] - x), Color(0, 127, 255))


    def render(self, surface: Surface, thickness: int, color: Color) -> None:
        x = 0
        y = self.radius
        m = 5 - 4 * self.radius
        
        while y >= x:
            self.render_pixels(surface, x, y, color)

            if m > 0:
                y -= 1
                m -= 8 * y

            x += 1
            m += 8 * x + 4
