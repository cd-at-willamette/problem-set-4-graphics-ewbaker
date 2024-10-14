########################################
# Name: Evyn Baker
# Collaborators: Myself and Calvins Slides
# Estimated time spent (hrs): 2 hrs
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 15

def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """
    
    gw = GWindow(WIDTH, HEIGHT)

    # Loop through each row (starting from the bottom)
    for row in range(BRICKS_IN_BASE):
        # Calculate how many bricks go in this row (fewer as we go up)
        bricks_in_row = BRICKS_IN_BASE - row
        # Figure out how much space we need to center the row
        x_offset = (WIDTH - (bricks_in_row * BRICK_WIDTH)) / 2
        # Set the y position for this row (stacking upwards)
        y = HEIGHT - (row + 1) * BRICK_HEIGHT
        
        # Time to place the bricks in the current row
        for brick in range(bricks_in_row):
            # Calculate the x position for each brick in the row
            x = x_offset + brick * BRICK_WIDTH
            # Create the brick, make it filled, and give it some color
            brick_rect = GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
            brick_rect.set_filled(True)
            brick_rect.set_color("orange")
            gw.add(brick_rect)

if __name__ == '__main__':
    draw_pyramid()



















if __name__ == '__main__':
    draw_pyramid()
