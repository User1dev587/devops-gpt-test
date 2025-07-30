import pygame

class Snake:
    def __init__(self, width, height):
        self.block_size = 20
        self.body = [(width // 2, height // 2)]
        self.direction = "RIGHT"
        self.new_direction = "RIGHT"
        self.grow_pending = False

    @property
    def head(self):
        return self.body[0]

    def change_direction(self, direction):
        valid_directions = {"UP", "DOWN", "LEFT", "RIGHT"}
        if direction not in valid_directions:
            return  # Ignore invalid directions
        opposite = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        if direction != opposite.get(self.direction):
            self.new_direction = direction

    def move(self):
        self.direction = self.new_direction
        x, y = self.head
        if self.direction == "UP":
            y -= self.block_size
        elif self.direction == "DOWN":
            y += self.block_size
        elif self.direction == "LEFT":
            x -= self.block_size
        elif self.direction == "RIGHT":
            x += self.block_size

        new_head = (x, y)
        self.body.insert(0, new_head)

        if self.grow_pending:
            self.grow_pending = False
        else:
            self.body.pop()

    def grow(self):
        self.grow_pending = True

    def check_collision(self, width, height):
        x, y = self.head
        if x < 0 or x >= width or y < 0 or y >= height:
            return True
        if self.head in self.body[1:]:
            return True
        return False

    def draw(self, screen):
        for segment in self.body:
            rect = pygame.Rect(segment[0], segment[1], self.block_size, self.block_size)
            pygame.draw.rect(screen, (0, 255, 0), rect)
