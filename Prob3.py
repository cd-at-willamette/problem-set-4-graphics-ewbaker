########################################
# Name: Evyn Baker
# Collaborators: Myself and Calvins Slides and also Math Tutors
# Estimate time spent (hrs): 4 1/2
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Window width
GW_HEIGHT = 500                     # Window height
SQUARE_SIZE = 50                    # Size of the square
SCORE_DX = 10                       # Distance from left of the window to origin (for the score label)
SCORE_DY = 10                       # Distance up from the bottom for the score label
SCORE_FONT = "bold 40pt 'serif'"    # Font style for the score

def clicky_box():

    # Callback function to handle mouse clicks (Part C)
    def on_mouse_down(event):
        # Randomly reposition the square
        new_x = random.uniform(0, GW_WIDTH - SQUARE_SIZE)
        new_y = random.uniform(0, GW_HEIGHT - SQUARE_SIZE)
        square.set_location(new_x, new_y)  # Move the square
        print(f"Square moved to: ({new_x}, {new_y})")  # Just so you know where it's moving

    # Create the window
    gw = GWindow(GW_WIDTH, GW_HEIGHT)

    # Draw the initial square in the center of the window
    initial_x = (GW_WIDTH - SQUARE_SIZE) / 2  # Center horizontally
    initial_y = (GW_HEIGHT - SQUARE_SIZE) / 2  # Center vertically
    square = GRect(initial_x, initial_y, SQUARE_SIZE, SQUARE_SIZE)
    square.set_filled(True)
    square.set_color("blue")  # Square starts as blue
    gw.add(square)

    # Add the mouse event listener to detect clicks
    gw.add_event_listener("mousedown", on_mouse_down)

if __name__ == '__main__':
    clicky_box()
