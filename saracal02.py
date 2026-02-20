import pygame 
pygame.init() # Initialize Pygame
screen = pygame.display. set_mode( (400, 300))
running = True
sara = pygame.image.load("sara/sara-cal1.png") # Load an image
sara_rect = pygame.Rect(0,0,34,56) # Create a rect for the image
sara_position = pygame.Rect(50, 50, 34, 56) # Initial position of the image
clock = pygame.time.Clock() # Create a clock object to control frame rate
while running: # Game Loop
    for event in pygame.event.get(): # Event handling
        if event.type == pygame.QUIT: # Check for quit event
            running = False
    key = pygame.key.get_pressed() # Get the state of all keyboard buttons
    if key[pygame.K_RIGHT] and sara_position.x + sara_rect.width < 400: # Move right
        sara_position.x += 5
    elif key[pygame.K_LEFT] and sara_position.x > 0: # Move left
        sara_position.x -= 5
    elif key[pygame.K_DOWN] and sara_position.y + sara_rect.height < 300: # Move down
        sara_position.y += 5
    elif key[pygame.K_UP] and sara_position.y > 0: # Move up
        sara_position.y -= 5
            
    clock.tick(90) # Limit to 60 FPS
    screen.fill((255, 255, 255)) # Fill the screen with white
    font = pygame.font.SysFont("Arial", 36) 
    text = font.render(f'FPS: {clock.get_fps():.2f}', True, (0, 0, 0)) # Render text
    screen.blit(text, (300, 230)) # Draw text on the screen
    screen.blit(sara, sara_position, sara_rect) # Draw the loaded image with the rect
    pygame.display.update() # Update the display
pygame.quit() # Quit Pygame