import pygame

SEGMENT_SIZE = 20
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Snake:
    def __init__(self):
        # Initialize snake starting position and body segments
        # Start with 3 segments horizontally centered
        start_x = SCREEN_WIDTH // 2
        start_y = SCREEN_HEIGHT // 2
        self.body = [
            pygame.Rect(start_x, start_y, SEGMENT_SIZE, SEGMENT_SIZE),
            pygame.Rect(start_x - SEGMENT_SIZE, start_y, SEGMENT_SIZE, SEGMENT_SIZE),
            pygame.Rect(start_x - 2 * SEGMENT_SIZE, start_y, SEGMENT_SIZE, SEGMENT_SIZE),
        ]
        # Set initial movement direction to right
        self.direction = (1, 0)  # (dx, dy)

    def move(self, direction):
        # Update snake position based on direction
        # direction is a tuple (dx, dy) where each is -1, 0, or 1
        if direction:
            # Prevent the snake from reversing directly
            opposite_direction = (-self.direction[0], -self.direction[1])
            if direction != opposite_direction:
                self.direction = direction

        dx, dy = self.direction
        # Calculate new head position
        new_head = self.body[0].copy()
        new_head.x += dx * SEGMENT_SIZE
        new_head.y += dy * SEGMENT_SIZE

        # Move body segments
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        # Add a new segment to the snake's body at the tail
        tail = self.body[-1]
        # Add a new segment at the same position as the last segment (it will follow on next move)
        new_segment = pygame.Rect(tail.x, tail.y, SEGMENT_SIZE, SEGMENT_SIZE)
        self.body.append(new_segment)

    def check_collision(self):
        # Check if snake collides with itself
        head = self.body[0]
        # Check collision with body
        for segment in self.body[1:]:
            if head.colliderect(segment):
                return True
        # Check collision with boundaries
        if (head.x < 0 or head.x >= SCREEN_WIDTH or
            head.y < 0 or head.y >= SCREEN_HEIGHT):
            return True
        return False

    def draw(self, surface):
        # Draw each segment of the snake on the given surface
        for segment in self.body:
            pygame.draw.rect(surface, (0, 255, 0), segment)
            # Draw a border for better visibility
            pygame.draw.rect(surface, (0, 100, 0), segment, 1)
