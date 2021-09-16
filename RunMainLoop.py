from animal import *


def run_main_loop(animals, world):
    for animal in animals:
        animal.do_move(world)