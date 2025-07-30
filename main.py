import pygame
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

if __name__ == "__main__":
    main()
