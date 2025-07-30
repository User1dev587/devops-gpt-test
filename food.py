import pygame
import random

class Food:
    def __init__(self, width, height, snake_body):
        self.block_size = 20
        self.width = width
        self.height = height
        self.position = (0, 0)
        self.spawn(snake_body)

    def spawn(self, snake_body):
        max_x = (self.width // self.block_size) - 1
        max_y = (self.height // self.block_size) - 1

        all_positions = [
            (x * self.block_size, y * self.block_size)
            for x in range(max_x + 1)
            for y in range(max_y + 1)
        ]
        free_positions = [pos for pos in all_positions if pos not in snake_body]

        if not free_positions:
            # No free position available; keep current position or handle as needed
            return

        self.position = random.choice(free_positions)

    def draw(self, screen):
        rect = pygame.Rect(self.position[0], self.position[1], self.block_size, self.block_size)
        pygame.draw.rect(screen, (255, 0, 0), rect)
