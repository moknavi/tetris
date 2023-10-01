import pygame
import create_tetromino

score = 0

pygame.init()
gui_surface = pygame.display.set_mode(size = (220, 440))
game_surface = pygame.display.set_mode(size = (200, 400))

def draw_gui(score):
    score_text = pygame.font.Font.render(f"Score: {score}".encode(), False, (255, 255, 255))
    gui_surface.blit(score_text, (0,0))
    pygame.display.flip()

while True:
    draw_gui(score)