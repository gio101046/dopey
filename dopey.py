import sys
from io import TextIOWrapper
from blessed import Terminal

class MismatchBracketException(Exception):
    """ TODO line number and column """
    pass

class Memory:
    BUFFER_SIZE = 30_000
    buffer = [0 for _ in range(BUFFER_SIZE)]
    pointer = 0

    @classmethod
    def get_pointer(cls) -> int:
        # TODO add logic to roll around buffer
        return cls.pointer

class Operation:
    SHIFT_LEFT = "<"
    SHIFT_RIGHT = ">"
    INCREMENT = "+"
    DECREMENT = "-"
    OUTPUT = "."
    INPUT = ","
    OPEN_LOOP = "["
    CLOSE_LOOP = "]"

    terminal = Terminal()
    loop_stack = []

    @classmethod
    def perform(cls, operation: str, file: TextIOWrapper) -> None:
        switch = {
            cls.SHIFT_LEFT: cls.shift_left,
            cls.SHIFT_RIGHT: cls.shift_right,
            cls.INCREMENT: cls.increment,
            cls.DECREMENT: cls.decrement,
            cls.OUTPUT: cls.output,
            cls.INPUT: cls.input,
            cls.OPEN_LOOP: cls.open_loop,
            cls.CLOSE_LOOP: cls.close_loop
        }

        if operation not in switch:
            return
        switch[operation](file)

    @classmethod
    def shift_left(cls, _) -> None:
        Memory.pointer -= 1
    
    @classmethod
    def shift_right(cls, _) -> None:
        Memory.pointer += 1

    @classmethod    
    def increment(cls, _) -> None:
        Memory.buffer[Memory.get_pointer()] += 1

    @classmethod
    def decrement(cls, _) -> None:
        Memory.buffer[Memory.get_pointer()] -= 1

    @classmethod
    def output(cls, _) -> None:
        print(chr(Memory.buffer[Memory.get_pointer()]), end="") # TODO rollover if too big in ASCII

    @classmethod
    def input(cls, _) -> None:
        with cls.terminal.cbreak():
            Memory.buffer[Memory.get_pointer()] = ord(cls.terminal.inkey())

    @classmethod
    def open_loop(cls, file: TextIOWrapper) -> None:
        if not Memory.buffer[Memory.get_pointer()]:
            while True:
                operation = file.read(1)
                if operation == Operation.CLOSE_LOOP:
                    break
                elif not operation:
                    raise MismatchBracketException
        else:
            cls.loop_stack.append(file.tell()-1)
    
    @classmethod
    def close_loop(cls, file: TextIOWrapper) -> None:
        if not len(cls.loop_stack):
            raise MismatchBracketException

        last_open_loop_pos = cls.loop_stack.pop()
        if Memory.buffer[Memory.get_pointer()]:
            file.seek(last_open_loop_pos, 0)

def main() -> None:
    file_location = None
    if len(sys.argv) != 2:
        print("Invalid or missing arguments...")
        sys.exit()
    else:
        file_location = sys.argv[1]

    file = open(file_location, "r")
    while True:
        operation = file.read(1)
        if not operation:
            break
        Operation.perform(operation, file)

    file.close()
    if len(Operation.loop_stack):
        raise MismatchBracketException

if __name__ == "__main__":
    main()

