import pygame


def drawTl(win, canvas_w, canvas_h, size):
    tile_size = size
    for line in range(0, 20):
        pygame.draw.line(win, (0, 0, 0), (0, line * tile_size), (canvas_w, line * tile_size))
        pygame.draw.line(win, (0, 0, 0), (line * tile_size, 0), (line * tile_size, canvas_h))

