
# create memory buffer
BUFFER_SIZE = 30_000
buffer = [0 for _ in range(BUFFER_SIZE)]

# define bf commands
SHIFT_LEFT = "<"
SHIFT_RIGHT = ">"
INCREMENT = "+"
DECREMENT = "-"
OUTPUT = "."
INPUT = ","
OPEN_LOOP = "["
CLOSE_LOOP = "]"