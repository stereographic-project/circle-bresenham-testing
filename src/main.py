from pygame import Surface, Color, K_SPACE
import pygame

from rendering import Circle

circle1 = Circle((500, 500), 302)
circle2 = Circle((500, 500), 301)
circle3 = Circle((500, 500), 300)
circle4 = Circle((500, 500), 299)
circle5 = Circle((500, 500), 298)

fps        = 10000
resolution = width, height = 1000, 1000
clock      = pygame.time.Clock()
surface    = pygame.display.set_mode(resolution)

while True:
    [exit() for event in pygame.event.get() if event.type == pygame.QUIT]
    clock.tick(fps)
    
    if pygame.key.get_pressed()[K_SPACE]:
        pygame.display.set_caption(f"Circle Bresenham: PAUSED")
        continue

    surface.fill(Color(0, 0, 0))

    pygame.display.set_caption(f"Circle Bresenham. { clock.get_fps() // 1 } FPS")
    
    print(f"1: { + pygame.time.get_ticks() }")
    circle1.render(surface, 2, Color(255, 255, 255))
    print(f"2: { + pygame.time.get_ticks() }")
    circle2.render(surface, 2, Color(255, 255, 255))
    print(f"3: { + pygame.time.get_ticks() }")
    circle3.render(surface, 2, Color(255, 255, 255))
    print(f"4: { + pygame.time.get_ticks() }")
    circle4.render(surface, 2, Color(255, 255, 255))
    print(f"5: { + pygame.time.get_ticks() }")
    circle5.render(surface, 2, Color(255, 255, 255))

    pygame.display.flip()