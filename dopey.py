import sys
from blessed import Terminal

# create memory buffer and pointer
class Memory:
    BUFFER_SIZE = 30_000
    buffer = [0 for _ in range(BUFFER_SIZE)]
    pointer = 0

    @classmethod
    def get_pointer(cls) -> int:
        # TODO add logic to roll around buffer
        return cls.pointer

# define bf commands
class Operation:
    SHIFT_LEFT = "<"
    SHIFT_RIGHT = ">"
    INCREMENT = "+"
    DECREMENT = "-"
    OUTPUT = "."
    INPUT = ","
    OPEN_LOOP = "["
    CLOSE_LOOP = "]"

def main() -> None:
    # get bf file location
    file_location = None
    if len(sys.argv) != 2:
        print("Invalid or missing arguments...")
        sys.exit()
    else:
        file_location = sys.argv[1]

    # open file
    file = open(file_location, "r")
    while True:
        operation = file.read(1)
        if not operation:
            break
        
        # perform operation
        perform_operation(operation)

    file.close()

def perform_operation(operation: str) -> None:
    if operation == Operation.SHIFT_LEFT:
        Memory.pointer -= 1
    elif operation == Operation.SHIFT_RIGHT:
        Memory.pointer += 1
    elif operation == Operation.INCREMENT:
        Memory.buffer[Memory.get_pointer()] += 1
    elif operation == Operation.DECREMENT:
        Memory.buffer[Memory.get_pointer()] -= 1
    elif operation == Operation.OUTPUT:
        print(chr(Memory.buffer[Memory.get_pointer()]), end="")
    elif operation == Operation.INPUT:
        term = Terminal()
        with term.cbreak():
            Memory.buffer[Memory.get_pointer()] = ord(term.inkey())

if __name__ == "__main__":
    main()

