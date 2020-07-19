# import modules
import time

# global identifiers
WIDTH, HEIGHT = 800, 600

moves = 0
time_start = 0
time_elapsed = 0
level = "5-1-10"

tube_list = []


def is_empty(tube):
    """Empty tube have no drops."""

    pass


def is_full(tube):
    """Full tube has four drops."""

    pass


def is_complete(tube):
    """Is the current tube complete?
       complete = is full and all drops have the same color."""

    pass


def is_all_complete():
    """Is all tubes complete (or empty)?"""

    pass


def put_drop(drop, tube, ignore_color=False):
    """Put given drop in given tube, optionaly ignoring color constraint."""

    # return early if move is not allowed
    pass

    # move allowed, so drop into given tube
    pass


def get_drop(tube):
    """Get top drop from given tube."""

    pass


def is_valid_move(drop, tube):
    """Return True if given drop can be put in given tube."""

    pass


def start_level():
    global tube_list
    global moves, time_start, time_elapsed

    # get/set level parameters
    n_colors, n_spare, n_difficulty = [int(v) for v in level.split("-")]
    n_total = n_colors + n_spare

    # create each tube and its drops
    for k in range(n_total):
        tube = Actor("tube", midbottom=( (k+1)*WIDTH//(n_total+1), HEIGHT-100) )
        tube_list.append(tube)

    # Shuffle starting position
    pass

    # reset level counters
    moves = 0
    time_start = time.time()

    time_elapsed = 0


def move_drop(tube):
    """Pick up/drop a drop from/to selected tube."""

    global moves

    moves += 1



def on_mouse_down(pos):
    """Select tube using mouse click."""

    move_drop(None)


def on_key_down(key):
    """Select tube using number keys."""

    if keyboard.space:
        move_drop(None)



def update():
    global time_elapsed, time_start

    time_elapsed = time.time() - time_start



def draw():
    global tube_list
    global level, moves, time_elapsed

    screen.clear()

    # HUD
    screen.draw.text("Test Tube Sort", midtop=(WIDTH//2, 5), color="orange", fontsize=70)
    screen.draw.text(f"Moves: {moves}", topleft=(5,5), fontsize=30)
    screen.draw.text(f"Time: {time_elapsed:7.2f}", topleft=(5,35), fontsize=30)
    screen.draw.text(f"Level: {level}", topright=(WIDTH-5,5), fontsize=30)

    # each tube (and its drops)
    for tube in tube_list:
        tube.draw()
    pass

    # picked drop
    pass

    # end of level/game message
    pass


start_level()
