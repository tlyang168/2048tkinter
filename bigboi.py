import random
import time

def generate_moves():
    """Create the sequences for big boi to move"""
    dirs = [1, 2, 3, 4]
    yield random.choice(dirs)
    yield from generate_moves()

def move(board):
    dirs = board.computer()
    gen = generate_moves()
    time.sleep(0.2)
    dirs[next(gen)]('e')


