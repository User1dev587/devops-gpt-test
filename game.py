import pygame
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        # Initialize all pygame modules (including font)
        pygame.init()

        # Screen and grid settings
        self.screen_width = 600
        self.screen_height = 600
        self.grid_size = 20
        self.grid_width = self.screen_width // self.grid_size
        self.grid_height = self.screen_height // self.grid_size

        # Initialize screen and clock
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()

        # Initialize font for score and messages
        self.font = pygame.font.SysFont("arial", 24, bold=True)

        # Initialize game objects
        self.snake = Snake(self.grid_width, self.grid_height)
        self.food = Food(self.grid_width, self.grid_height, self.grid_size)
        self.food.respawn(self.snake.body)

        # Game state variables
        self.score = 0
        self.speed = 10  # Initial speed (frames per second)
        self.running = True
        self.game_over_flag = False

    def run(self):
        while self.running:
            self.handle_input()
            if not self.game_over_flag:
                self.update()
            self.render()
            self.clock.tick(self.speed)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if not self.game_over_flag:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction("UP")
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction("DOWN")
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction("LEFT")
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction("RIGHT")
                else:
                    # On game over screen, allow restart or quit
                    if event.key == pygame.K_r:
                        self.reset()
                    elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        self.running = False

    def update(self):
        self.snake.move()

        # Check collisions
        self.check_collisions()

    def render(self):
        # Clear screen with black
        self.screen.fill((0, 0, 0))

        # Draw snake and food
        self.snake.draw(self.screen)
        self.food.draw(self.screen)

        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        # Draw difficulty level (speed)
        level = (self.speed - 10) // 2 + 1
        level_text = self.font.render(f"Level: {level}", True, (255, 255, 255))
        self.screen.blit(level_text, (self.screen_width - 120, 10))

        # If game over, show game over screen
        if self.game_over_flag:
            self.game_over()

        pygame.display.flip()

    def check_collisions(self):
        head_pos = self.snake.get_head_position()

        # Check collision with food
        if head_pos == self.food.position:
            self.snake.grow()
            self.score += 1
            self.food.respawn(self.snake.body)

            # Increase difficulty every 5 points, max speed 30
            if self.score % 5 == 0 and self.speed < 30:
                self.speed += 2

        # Check collision with walls
        x, y = head_pos
        if x < 0 or x >= self.grid_width or y < 0 or y >= self.grid_height:
            self.game_over_flag = True

        # Check collision with self
        if self.snake.check_self_collision():
            self.game_over_flag = True

    def game_over(self):
        # Overlay semi-transparent black
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))

        # Render game over text
        game_over_text = self.font.render("GAME OVER", True, (255, 0, 0))
        restart_text = self.font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))
        final_score_text = self.font.render(f"Final Score: {self.score}", True, (255, 255, 255))

        # Center texts
        go_rect = game_over_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 40))
        rs_rect = restart_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
        fs_rect = final_score_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 40))

        self.screen.blit(game_over_text, go_rect)
        self.screen.blit(restart_text, rs_rect)
        self.screen.blit(final_score_text, fs_rect)

    def reset(self):
        # Reset game state for restart
        self.snake = Snake(self.grid_width, self.grid_height)
        self.food.respawn(self.snake.body)
        self.score = 0
        self.speed = 10
        self.game_over_flag = False
