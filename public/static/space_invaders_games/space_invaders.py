WIDTH, HEIGHT = 800, 600
from random import randint

# global game data

level = 1
score = 0
rows, cols = 3, 7
speed = 2

ship = Actor("ship", midbottom=(WIDTH // 2, HEIGHT - 10))
ship.time_to_fire = 0

ship_rockets = []

blocks = []

invaders = []
invader_rockets = []


def setup_level():
    """Create level objects - invaders and blocks."""

    global level, rows, cols

    # create invader horde
    for row in range(rows):
        for col in range(cols):
            invader = Actor("invader_0_0", pos=(80+90*col,80+60*row))
            invader.isAlive = True
            invaders.append(invader)

    # create blocks
    n = 9
    for k in range(n):
        block = Actor("block_0", pos=( (k+0.5)*WIDTH//n ,HEIGHT-100))
        block.isAlive = True
        blocks.append(block)



def update(dt):
    """Update all game objects and respoence to used input."""

    global score, level, speed, invaders, invader_rockets, ship, ship_rockets, blocks, pause

    # STEP 0
    ship.time_to_fire -= dt

    # STEP 1 - update invader horde

    # determine direction - left to right and down at every turn
    xs = [invader.x for invader in invaders]
    if (min(xs)<40 and speed<0) or (max(xs)>WIDTH-50 and speed>0):
        speed = -speed
        dy = 20
    else:
        dy = 0

    # move each invader and fire at random
    for invader in invaders:
        invader.x += speed
        invader.y += dy
        if randint(1,100) == 1:
            rocket = Actor("invader_rocket", pos=invader.pos)
            rocket.isAlive = True
            invader_rockets.append(rocket)



    # STEP 2 - check for game over due to invaders reaching the ground
    pass

    # STEP 3 - update ship position and fire
    if keyboard.left and ship.midleft[0]>10:
        ship.x -= 10
    if keyboard.right and ship.midright[0]<WIDTH-10:
        ship.x += 10
    if keyboard.space and ship.time_to_fire<=0:
        rocket = Actor("ship_rocket", pos=ship.pos)
        #sounds.ship_fired.play()
        rocket.isAlive = True
        ship_rockets.append(rocket)
        ship.time_to_fire = 0.1

    # STEP 4 - move ship rockets amd invader rockets
    for rocket in ship_rockets:
        rocket.y -= 10
    for rocket in invader_rockets:
        rocket.y += 10

    # STEP 5 - collision detection

    # ship_rockets and blocks - optional
    pass

    # ship_rockets and invaders
    pass

    # invader_rockets and blocks
    pass

    # invader_rockets and ship
    pass

    # STEP 6 - clean up/remove dead objects
    ship_rockets = [r for r in ship_rockets if r.y>60]
    invader_rockets = [r for r in invader_rockets if r.y<HEIGHT-10]



def draw():
    """Draw HUD and game objects."""

    global score, level

    # STEP 1 - HUD
    screen.clear()
    screen.draw.text("Score %s" % score, topleft=(5,10), fontname="unifont")
    screen.draw.text("Space Invaders", midtop=(WIDTH//2, 0), color="orange", fontsize=40, fontname="unifont")
    screen.draw.text("Level %s" % level, topright=(WIDTH-5,10), fontname="unifont")

    # STEP 2 - game objects
    for rocket in ship_rockets:
        rocket.draw()
    for rocket in invader_rockets:
        rocket.draw()
    for block in blocks:
        block.draw()
    for invader in invaders:
        invader.draw()

    ship.draw()



# finally start game
setup_level()
