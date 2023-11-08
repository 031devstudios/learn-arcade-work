"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.

Multi-line comments are surrounded by three double-quote marks.
Single-line comments start with a hash/pound sign. #
"""

# Import the "arcade" library

import arcade

arcade.open_window(600, 600, "Drawing Example")

# Set background colour
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Finish drwaing
arcade.finish_render()

# Keep the window open
arcade.run()