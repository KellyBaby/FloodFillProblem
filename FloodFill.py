from pickle import NONE
from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    # Implement your code here.


    def hahaha (r,c):
        if input_board[r][c] != old:
            return None
        else:
            input_board[r] = input_board[r][:c] + new + input_board[r][c+1:]

            if r > 0:
                hahaha(r-1,c)
            if r + 1 < len(input_board):
                hahaha(r+1,c)
            if c > 0:
                hahaha(r,c-1)
            if c + 1 > len(input_board):
                hahaha(r,c+1)

    hahaha(x,y)
    return input_board


modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....

I think your code is very clear!!