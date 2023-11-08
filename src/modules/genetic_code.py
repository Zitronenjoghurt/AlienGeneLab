import numpy as np

# Configuration
CODE_LENGTH = 4
CODE = {0: 'A', 1: 'G', 2: 'C', 3: 'T'}

# Precalculation
REVERSED_CODE = {value: key for key, value in CODE.items()}
INDICES = np.array(list(CODE.keys()))
VALUES = set(CODE.values())

def encode(values: list) -> str:
    result = [to_base4(value) for value in values]
    return ''.join(result)

def decode(code: str) -> list:
    code = code.upper()
    code = ''.join(filter(VALUES.__contains__, code))

    block_count = len(code) // CODE_LENGTH
    result = [None] * block_count
    
    for i in range(block_count):
        block = code[i*CODE_LENGTH:(i+1)*CODE_LENGTH]
        result[i] = from_base4(block)
    
    return result

def to_base4(value: int) -> str:
    result = [CODE[0]] * CODE_LENGTH
    
    index = CODE_LENGTH - 1
    
    while value > 0 and index >= 0:
        remainder = value % 4
        result[index] = CODE[remainder]
        value //= 4
        index -= 1

    return ''.join(result)

def from_base4(string: str) -> int:
    value = 0
    power = 1

    for char in string[::-1]:
        value += REVERSED_CODE[char] * power
        power *= CODE_LENGTH
    
    return value

def base4_sum(string: str) -> int:
    result = 0

    for char in string:
        result += REVERSED_CODE.get(char, 0)
    
    return result

def count_char(string: str, char: str) -> int:
    result = 0

    for character in string:
        if character == char:
            result += 1

    return result

# chance between 0 and 1
def flip_code(code: str, chance: float) -> str:
    result = [flip_char(char) if np.random.rand() < chance else char for char in code]
    return ''.join(result)

def flip_char(char: str) -> str:
    indices = INDICES[INDICES != REVERSED_CODE[char]]
    return CODE[np.random.choice(indices)]