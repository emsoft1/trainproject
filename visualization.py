import pygame

def initialize_screen(width, height):
    pygame.init()
    return pygame.display.set_mode((width, height))

def draw_simulation(screen, track, train):
    screen.fill((255, 255, 255))  # Clear with white background
    # Drawing logic here (track, train, measurement points)
    pygame.display.flip()
