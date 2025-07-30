import pygame

class Snake:
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
        else:
            self.body.pop()

    def grow(self):
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
