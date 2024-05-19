import sys

sys.path.append("./src")
from board import Board


p = Board()
p.generate_tile()
print(p)
