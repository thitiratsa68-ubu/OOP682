import pygame 
pygame.init() # Initialize Pygame
screen = pygame.display. set_mode( (400, 300))
running = True
while running: # Game Loop
    pygame.time.delay(100) # Delay to control frame rate
    pygame.display.update()