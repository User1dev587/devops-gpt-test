import pygame
import sys
from snake import Snake
from food import Food

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SEGMENT_SIZE = 20
INITIAL_SPEED = 10
MAX_SPEED = 25
SPEED_INCREMENT_SCORE = 5  # Increase speed every 5 points

def draw_text(text, font, color, surface, x, y):
    """Render text on the given surface at specified coordinates."""
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 24)
    large_font = pygame.font.SysFont("arial", 48)

    while True:
        # Initialize game variables
        snake = Snake()
        food = Food()
        food.reposition(snake.body)
        score = 0
        speed = INITIAL_SPEED
        game_over = False
        direction = (1, 0)  # Start moving right

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if direction != (0, 1):
                            direction = (0, -1)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if direction != (0, -1):
                            direction = (0, 1)
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if direction != (1, 0):
                            direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if direction != (-1, 0):
                            direction = (1, 0)

            snake.move(direction)

            # Check for collision with food
            if snake.body[0].colliderect(food.rect):
                snake.grow()
                score += 1
                food.reposition(snake.body)

                # Increase speed every SPEED_INCREMENT_SCORE points, capped at MAX_SPEED
                if score % SPEED_INCREMENT_SCORE == 0 and speed < MAX_SPEED:
                    speed += 1

            # Check for collision with self or boundaries
            if snake.check_collision():
                game_over = True

            # Draw everything
            screen.fill((0, 0, 0))  # Clear screen with black
            snake.draw(screen)
            food.draw(screen)
            draw_text(f"Score: {score}", font, (255, 255, 255), screen, 10, 10)

            pygame.display.flip()
            clock.tick(speed)

        # Game over screen
        screen.fill((0, 0, 0))
        draw_text("Game Over!", large_font, (255, 0, 0), screen, SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 - 60)
        draw_text(f"Final Score: {score}", font, (255, 255, 255), screen, SCREEN_WIDTH // 2 - 70, SCREEN_HEIGHT // 2)
        draw_text("Press R to Restart or Q to Quit", font, (255, 255, 255), screen, SCREEN_WIDTH // 2 - 140, SCREEN_HEIGHT // 2 + 40)
        pygame.display.flip()

        # Wait for user input to restart or quit
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        waiting = False  # Restart game
                    elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

if __name__ == "__main__":
    main()
