import pygame
<<<<<<< HEAD
from game import Game

def main():
    try:
        pygame.init()  # Initialize all imported pygame modules
        game = Game()
        game.run()
    finally:
        pygame.quit()  # Ensure pygame quits properly
=======
import sys
from game import Game

def main():
    pygame.init()
    game = Game()
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and game.is_game_over():
                    pygame.quit()
                    sys.exit()
            game.handle_input(event)

        game.update()
        game.render()
        pygame.display.flip()
        clock.tick(game.speed)
>>>>>>> 47ced9037636ddd2f2b11b56bd6c1205b25b73b5

if __name__ == "__main__":
    main()
