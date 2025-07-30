import pygame
import random

class Food:
<<<<<<< HEAD
    def __init__(self, grid_width, grid_height, grid_size):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.grid_size = grid_size
        self.position = (0, 0)
        self.color = (255, 0, 0)
        self.respawn([])

    def respawn(self, snake_positions):
        while True:
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)
            if (x, y) not in snake_positions:
                self.position = (x, y)
                break

    def draw(self, surface):
        x, y = self.position
        rect = pygame.Rect(x * self.grid_size, y * self.grid_size, self.grid_size, self.grid_size)
        pygame.draw.rect(surface, self.color, rect)
        # Draw a darker border for better visibility
        pygame.draw.rect(surface, (150, 0, 0), rect, 1)
=======
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
>>>>>>> 47ced9037636ddd2f2b11b56bd6c1205b25b73b5
