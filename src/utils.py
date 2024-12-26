import pygame
import random

COLORS = {
    "background": (30, 30, 30),
    "bar": (100, 200, 100),
    "bar_highlight": (200, 100, 100),
    "text": (255, 255, 255)
}


def generate_array(size, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(size)]


def draw_array(screen, array):
    width = screen.get_width()
    height = screen.get_height()
    bar_width = width // len(array)
    max_val = max(array)

    for i, val in enumerate(array):
        bar_height = int((val / max_val) * (height - 50))
        x = i * bar_width
        y = height - bar_height

        pygame.draw.rect(screen, COLORS["bar"], (x, y, bar_width, bar_height))
