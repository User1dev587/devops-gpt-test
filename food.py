import pygame
import random

SEGMENT_SIZE = 20
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Food:
    def __init__(self):
        # Initialize food position randomly within game boundaries
        self.rect = pygame.Rect(0, 0, SEGMENT_SIZE, SEGMENT_SIZE)
        self.reposition([])  # Initially no snake body to avoid

    def reposition(self, snake_body):
        max_x = (SCREEN_WIDTH // SEGMENT_SIZE) - 1
        max_y = (SCREEN_HEIGHT // SEGMENT_SIZE) - 1
        while True:
            x = random.randint(0, max_x) * SEGMENT_SIZE
            y = random.randint(0, max_y) * SEGMENT_SIZE
            self.rect.topleft = (x, y)
            # Check overlap with snake body using any() for optimization
            if not any(self.rect.colliderect(segment) for segment in snake_body):
                break

    def draw(self, surface):
        # Draw the food item on the given surface
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        # Draw a border for better visibility
        pygame.draw.rect(surface, (150, 0, 0), self.rect, 1)
