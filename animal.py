from AnimalActions import *
class Animal:
    def __init__(self, id):
        self.move_count = 0
        self.id = id
        self.x = 0

        self.actions = {
            ACTION_NONE: lambda i: pass,
            ACTION_MOVE_RIGHT: lambda i: self.x += 1
        }
    def inner_move(self, world):
        return ACTION_NONE

    def do_move(self, world):
        self.move_count += 1
        print(f"Animal {self.id} move {self.move_count}")
        action = inner_move(world)
        self.actions.get(action)(animal)

            case ACTION_MOVE_RIGHT:
                self.x += 1
        return True
