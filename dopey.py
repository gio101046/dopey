import sys

# create memory buffer and pointer
class Memory:
    BUFFER_SIZE = 30_000
    buffer = [0 for _ in range(BUFFER_SIZE)]
    pointer = 0

    @classmethod
    def get_pointer(cls) -> int:
        pass

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
        pass
    elif operation == Operation.DECREMENT:
        pass
    elif operation == Operation.OUTPUT:
        pass
    elif operation == Operation.INPUT:
        pass

if __name__ == "__main__":
    main()

