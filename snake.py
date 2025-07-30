import pygame

class Snake:
<<<<<<< HEAD
    def __init__(self, grid_width, grid_height):
        # Start in the middle of the grid with 3 segments
        start_x = grid_width // 2
        start_y = grid_height // 2
        self.body = [(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)]
        self.direction = "RIGHT"
        self.grow_flag = False
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.alive = True  # Flag to indicate if snake is alive (no boundary collision)

    def move(self):
        if not self.alive:
            return  # Do not move if snake is dead

        head_x, head_y = self.body[0]

        if self.direction == "UP":
            new_head = (head_x, head_y - 1)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + 1)
        elif self.direction == "LEFT":
            new_head = (head_x - 1, head_y)
        elif self.direction == "RIGHT":
            new_head = (head_x + 1, head_y)
        else:
            new_head = (head_x, head_y)  # Should not happen

        # Check boundary collision
        if not (0 <= new_head[0] < self.grid_width and 0 <= new_head[1] < self.grid_height):
            self.alive = False
            return

        self.body.insert(0, new_head)

        if self.grow_flag:
            self.grow_flag = False
=======
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
>>>>>>> 47ced9037636ddd2f2b11b56bd6c1205b25b73b5
        else:
            self.body.pop()

    def grow(self):
<<<<<<< HEAD
        self.grow_flag = True

    def change_direction(self, new_direction):
        # Prevent reversing direction
        opposites = {
            "UP": "DOWN",
            "DOWN": "UP",
            "LEFT": "RIGHT",
            "RIGHT": "LEFT"
        }
        if new_direction != opposites.get(self.direction):
            self.direction = new_direction

    def check_self_collision(self):
        head = self.body[0]
        return head in self.body[1:]

    def get_head_position(self):
        return self.body[0]

    def draw(self, surface, segment_size=20):
        # Draw each segment as a green square
        segment_color = (0, 255, 0)

        for segment in self.body:
            x, y = segment
            rect = pygame.Rect(x * segment_size, y * segment_size, segment_size, segment_size)
            pygame.draw.rect(surface, segment_color, rect)
            # Draw a darker border for better visibility
            pygame.draw.rect(surface, (0, 100, 0), rect, 1)
=======
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
>>>>>>> 47ced9037636ddd2f2b11b56bd6c1205b25b73b5
