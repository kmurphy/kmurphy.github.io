# imports of useful functions
from random import randint  # randint(a,b)       picks random integer between a and b
from random import choice  # choice(collection) picks a random element from a collection
import string

# game date

WIDTH, HEIGHT = 800, 600

words = ["dog", "cat", "banana"]
nodes = []  # was called dots
edges = []  # was called lines
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
    word = choice(words)
    print("Current word is", word)

    # STEP 2 - generate extra random dots based on the level
    pass

    # STEP 3 - generate random dots to store word
    for letter in word:
        node = Actor("big_blue_dot")
        node.pos = randint(20, WIDTH-20), randint(60, HEIGHT-20)
        node.label = letter
        node.used = False
        nodes.append(node)



def update():
    """Function to update game variables."""

    pass


def draw():
    """Function to draw screen."""

    global nodes, edges, previous_node
    global word, level

    # STEP 1 - Clear the screen
    screen.fill("black")

    # STEP 2 - Draw title and HUD
    screen.draw.text("10 Words", midtop=(WIDTH//2,0), color="orange", fontsize=60)
    screen.draw.text(f"Level {level}", bottomright=(WIDTH-10,40), color="green", fontsize=40)
    screen.draw.text(word, bottomleft=(10,40), color="pink", fontsize=40)

    # STEP 3 - Draw nodes
    for node in nodes:
        node.draw()
        screen.draw.text(node.label, center=node.pos, color="black", fontsize=40)

    # STEP 4 - Draw edges
    for edge in edges:
        start, end = edge
        screen.draw.line(start, end, (255,255,0))



def on_mouse_down(pos):
    """Function to respond to mouse click events."""

    global nodes, edges, previous_node
    global level, word, next_letter

    # CHECK - hit a correct node?
    for node in nodes:                  # checking each node
        # SUCCESS = node has correct letter AND node not used before AND mouse clicked on it
        if node.label==word[next_letter] and node.used==False and node.collidepoint(pos):
            print("HIT")
            sounds.shoot.play()
            if previous_node is not None:
                edges.append( (previous_node.pos, node.pos) )
            next_letter += 1
            previous_node = node

            break
    else:
        print("MISS")
        sounds.wet_splat.play()


    # CHECK - Win level ?
    pass


start()

