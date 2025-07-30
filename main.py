import pygame
from game import Game

def main():
    try:
        pygame.init()  # Initialize all imported pygame modules
        game = Game()
        game.run()
    finally:
        pygame.quit()  # Ensure pygame quits properly

if __name__ == "__main__":
    main()
