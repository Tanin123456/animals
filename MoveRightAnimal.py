from animal import *


class MoveRightAnimal(Animal):
    '''
    An Animal that only moves right.
    '''
    def inner_move(self, world):
        return ACTION_MOVE_RIGHT

