# imports of useful functions
from random import randint  # randint(a,b)       picks random integer between a and b
from random import choice  # choice(collection) picks a random element from a collection
import string

# game date

WIDTH, HEIGHT = 800, 600

words = ["dog", "cat", "banana"]
nodes = []
edges = []
previous_node = None
level = 0
next_letter = 0


def start():
    """Function to start game (or new level)."""

    global nodes, edges, previous_node
    global level, words, word, next_letter

    # STEP 0 - reset data
    pass

    # STEP 1 - pick a random word
    pass

    # STEP 2 - generate extra random dots based on the level
    pass

    # STEP 3 - generate random dots to store word
    pass


def update():
    """Function to update game variables."""

    pass


def draw():
    """Function to draw screen."""

    global nodes, edges, previous_node
    global word, level

    # STEP 1 - Clear the screen
    pass

    # STEP 2 - Draw title and HUD
    pass

    # STEP 3 - Draw nodes
    pass

    # STEP 4 - Draw edges
    pass


def on_mouse_down(pos):
    """Function to respond to mouse click events."""

    global nodes, edges, previous_node
    global level, word, next_letter

    # CHECK - hit a correct node?
    pass

    # CHECK - Win level ?
    pass


start()

