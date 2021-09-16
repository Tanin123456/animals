from Tests.TestCases.TestBase import Test
from RunMainLoop import run_main_loop
from globals import *

class AllAnimalsRun(Test):
    def __init__(self):
        self.description = "All animals run"

    def run():
        run_main_loop(animals, world)
        for animal in animals:
            if animal.move_count != 1:
                return False
        return True