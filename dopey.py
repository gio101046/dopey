import sys

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

# get bf file location
file_location = None
if len(sys.argv) != 2:
    print("Invalid or missing arguments...")
    sys.exit()
else:
    file_location = sys.argv[1]

# open file
file = open(file_location, "r")
print(file.read(1))



