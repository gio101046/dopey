import os
import sys
from io import TextIOWrapper
from typing import Dict, List

class MismatchBracketException(Exception):
    """ TODO line number and column """
    pass

class MemoryException(Exception):
    """ TODO line number and column """
    pass

class Memory:
    BUFFER_SIZE = 300_000
    buffer = [0 for _ in range(BUFFER_SIZE)]
    pointer = 0
    input_buffer = []

    @classmethod
    def get_pointer(cls) -> int:
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

    loop_stack = []

    @classmethod
    def perform(cls, operation: str, program: List, switch: Dict) -> None:
        if operation not in switch:
            return
        switch[operation](program)

    @classmethod
    def shift_left(cls, _) -> None:
        Memory.pointer -= 1
        if Memory.pointer < 0:
            raise MemoryException
    
    @classmethod
    def shift_right(cls, _) -> None:
        Memory.pointer += 1
        if Memory.pointer >= Memory.BUFFER_SIZE:
            raise MemoryException

    @classmethod    
    def increment(cls, _) -> None:
        Memory.buffer[Memory.get_pointer()] += 1

    @classmethod
    def decrement(cls, _) -> None:
        Memory.buffer[Memory.get_pointer()] -= 1

    @classmethod
    def output(cls, _) -> None:
        sys.stdout.write(chr(Memory.buffer[Memory.get_pointer()])) # TODO rollover if too big in ASCII

    @classmethod
    def input(cls, _) -> None:
        # flush text to terminal before asking for input
        sys.stdout.flush()

        if not len(Memory.input_buffer):
            input_ = sys.stdin.readline()
            Memory.input_buffer += list(input_)
        if len(Memory.input_buffer):
            Memory.buffer[Memory.get_pointer()] = ord(Memory.input_buffer.pop(0))

    @classmethod
    def open_loop(cls, program: List) -> None:
        if not Memory.buffer[Memory.get_pointer()]:
            # TODO redo this section to be more readable
            stack = [Operation.OPEN_LOOP]
            while program[1] < len(program[0]):
                operation = program[0][program[1]] 
                program[1] += 1
                if operation == Operation.CLOSE_LOOP: 
                    stack.pop()
                    if not len(stack):
                        return
                elif operation == Operation.OPEN_LOOP:
                    stack.append(Operation.OPEN_LOOP)
            raise MismatchBracketException
        else:
            cls.loop_stack.append(program[1]-1)
    
    @classmethod
    def close_loop(cls, program: List) -> None:
        if not len(cls.loop_stack):
            raise MismatchBracketException

        last_open_loop_pos = cls.loop_stack.pop()
        if Memory.buffer[Memory.get_pointer()]:
            program[1] = last_open_loop_pos

    def get_operations_in_switch() -> Dict:
        return {
            Operation.SHIFT_LEFT: Operation.shift_left,
            Operation.SHIFT_RIGHT: Operation.shift_right,
            Operation.INCREMENT: Operation.increment,
            Operation.DECREMENT: Operation.decrement,
            Operation.OUTPUT: Operation.output,
            Operation.INPUT: Operation.input,
            Operation.OPEN_LOOP: Operation.open_loop,
            Operation.CLOSE_LOOP: Operation.close_loop
        }

def main() -> None:
    file_location = None
    if len(sys.argv) != 2:
        print("Invalid or missing arguments...")
        sys.exit()
    else:
        file_location = sys.argv[1]

    file = open(file_location, "r")
    program = [file.read(), 0] # TODO create files class
    file.close()

    switch = Operation.get_operations_in_switch()

    while program[1] < len(program[0]):
        operation = program[0][program[1]]
        program[1] += 1
        Operation.perform(operation, program, switch)

    if len(Operation.loop_stack):
        raise MismatchBracketException

if __name__ == "__main__":
    main()

