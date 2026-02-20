import pygame 
pygame.init() # Initialize Pygame
screen = pygame.display. set_mode( (400, 300))
running = True
sara = pygame.image.load("sara/sara-cal1.png") # Load an image
clock = pygame.time.Clock() # Create a clock object to control frame rate
while running: # Game Loop
    for event in pygame.event.get(): # Event handling
        if event.type == pygame.QUIT: # Check for quit event
            running = False
    clock.tick(90) # Limit to 60 FPS
    screen.fill((255, 255, 255)) # Fill the screen with white
    font = pygame.font.SysFont("Arial", 36) 
    text = font.render(f'FPS: {clock.get_fps():.2f}', True, (0, 0, 0)) # Render text
    screen.blit(text, (300, 230)) # Draw text on the screen
    screen.blit(sara, (50, 50)) # Draw the loaded image
    pygame.display.update() # Update the display
pygame.quit() # Quit Pygame