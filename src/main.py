import pygame
from globals import BLACK
from globals import WHITE
from globals import segment_width
from globals import segment_height
from globals import segment_margin
from segment import Segment

# Set initial speed
x_change = segment_width + segment_margin
y_change = 0
speed = 5

# initial length
start_length = 15
length = 0

# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

# Set the title of the window
pygame.display.set_caption('Snake')

sprites_list = pygame.sprite.Group()
snake_segments = []

def speed_multiplier():
    global length
    multiplier = 1

    if (length < 20):
        multiplier = 1.010
    elif (length < 25):
        multiplier = 1.25
    elif (length < 30):
        multiplier = 1.40
    elif (length < 50):
        multiplier = 1.5
    else:
        multiplier = 1

    return multiplier

def grow():
    global speed, length
    x = 250 - (segment_width + segment_margin) * i
    y = 30
    segment = Segment(x, y)
    snake_segments.append(segment)
    sprites_list.add(segment)
    length += 1
    if (length > 15):
        speed = speed * speed_multiplier()

# Create an initial snake
for i in range(start_length):
    grow()

clock = pygame.time.Clock()
done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        # We want the speed to be enough that we move a full
        # segment, plus the margin.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                grow()
                x_change = (segment_width + segment_margin) * -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                grow()
                x_change = (segment_width + segment_margin)
                y_change = 0
            if event.key == pygame.K_UP:
                grow()
                x_change = 0
                y_change = (segment_height + segment_margin) * -1
            if event.key == pygame.K_DOWN:
                grow()
                x_change = 0
                y_change = (segment_height + segment_margin)

    # Get rid of last segment of the snake
    # .pop() command removes last item in list
    old_segment = snake_segments.pop()
    sprites_list.remove(old_segment)

    # Figure out where new segment will be
    x = snake_segments[0].rect.x + x_change
    y = snake_segments[0].rect.y + y_change
    segment = Segment(x, y)

    # Insert new segment into the list
    snake_segments.insert(0, segment)
    sprites_list.add(segment)

    # -- Draw everything
    # Clear screen
    screen.fill(BLACK)

    sprites_list.draw(screen)

    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(speed)

pygame.quit()
