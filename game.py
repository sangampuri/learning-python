# Import library code
from asyncio import run
from cmath import rect
from textwrap import fill

from django.contrib.admin import site

from random import randint

# The mouse_pressed function goes here



# The shoot_arrow function goes here



def setup():
    # Setup your game here
    site(400, 400)


def draw():
    # Things to do in every frame
    fill('cyan')
    rect(0, 0, 400, 250)


# Keep this to run your code
run(frame_rate=2)