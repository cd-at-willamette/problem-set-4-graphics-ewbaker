############################################################
# Name: Evyn Baker
# Name(s) of anyone worked with: Myself and Calvins Slides
# Est time spent (hr): 1 1/2 hrs
############################################################

from pgl import GWindow, GRect, GLine

# Setting up the window size (tweak if you want a bigger or smaller canvas)
WIDTH = 600
HEIGHT = 600

def draw_image():
    """ Draws a simple house, my take on 'architecture' """
    
    # Create the window (our drawing space)
    gw = GWindow(WIDTH, HEIGHT)

    # Draw the base of the house (big ol' rectangle)
    house_base = GRect(200, 300, 200, 200)
    house_base.set_filled(True)
    house_base.set_color("brown")  # Making the house base brown
    gw.add(house_base)

    # Draw the roof (lines forming a triangle, because why not)
    roof_left = GLine(200, 300, 300, 200)  # Left side of the roof
    roof_right = GLine(300, 200, 400, 300)  # Right side of the roof
    gw.add(roof_left)
    gw.add(roof_right)

    # Adding the door (because, obviously, houses need doors)
    door = GRect(275, 400, 50, 100)
    door.set_filled(True)
    door.set_color("black")  # The classic black door look
    gw.add(door)

if __name__ == '__main__':
    draw_image()
