import pygame
import random
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        self.width = 600
        self.height = 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        self.snake = Snake(self.width, self.height)
        self.food = Food(self.width, self.height, self.snake.body)
        self.score = 0
        self.speed = 10
        self.font = pygame.font.SysFont(None, 36)
        self.game_over = False
        self.clock = pygame.time.Clock()

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.snake.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                self.snake.change_direction("DOWN")
            elif event.key == pygame.K_LEFT:
                self.snake.change_direction("LEFT")
            elif event.key == pygame.K_RIGHT:
                self.snake.change_direction("RIGHT")
            elif event.key == pygame.K_ESCAPE:
                if self.game_over:
                    pygame.quit()
                    exit()
            elif event.key == pygame.K_r:
                if self.game_over:
                    self.restart()

    def update(self):
        if self.game_over:
            return

        self.snake.move()

        if self.snake.head == self.food.position:
            self.snake.grow()
            self.score += 1
            self.food.spawn(self.snake.body)
            if self.score % 5 == 0:
                self.speed += 1

        if self.snake.check_collision(self.width, self.height):
            self.game_over = True

    def render(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        if self.game_over:
            game_over_text = self.font.render("Game Over! Press R to restart or ESC to quit.", True, (255, 0, 0))
            rect = game_over_text.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(game_over_text, rect)

        pygame.display.flip()
        self.clock.tick(self.speed)

    def restart(self):
        self.snake = Snake(self.width, self.height)
        self.food.spawn(self.snake.body)
        self.score = 0
        self.speed = 10
        self.game_over = False
