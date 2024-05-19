import sys

sys.path.append("./src")
from board import Board


p = Board()
p.gen_board()
print(p)
