import pygame
import tetromino

score = 0
falling_distance = 0

def translateGameCordsIntoScreenCords(coords):
    coords[0] = coords[0]*40
    coords[1] = coords[1]*40
    return coords

pygame.init()
gui_surface = pygame.display.set_mode(size = (220, 440))
game_surface = pygame.display.set_mode(size = (200, 400))

def draw_gui(score):
    score_text = pygame.font.Font.render(pygame.font.Font(), f"Score: {score}".encode(), False, (255, 255, 255))
    gui_surface.blit(score_text, (0,0))
    pygame.display.flip()

#Game loop
running = True
while running:
    draw_gui(score)