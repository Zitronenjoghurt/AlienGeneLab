CODE = {0: 'A', 1: 'G', 2: 'C', 3: 'T'}
REVERSED_CODE = {value: key for key, value in CODE.items()}

CODE_LENGTH = 4

def encode(values: list) -> str:
    result = ""

    for value in values:
        result += to_base4(value)
    
    return result

def decode(code: str) -> list:
    # Uppercase and filter code
    code = code.upper()
    code = ''.join([char for char in code if char in CODE.values()])

    # Split code into equally sized blocks
    values = [code[i:i+CODE_LENGTH] for i in range(0, len(code), CODE_LENGTH)]

    result = []
    for value in values:
        result.append(from_base4(value))
    
    return result

def to_base4(value: int) -> str:
    if value == 0:
        return CODE[0]*4
    
    result = []
    while value > 0:
        remainder = value % 4
        result.append(CODE[remainder])
        value = value // 4

    base4 = ''.join(reversed(result))
    return base4.rjust(CODE_LENGTH, CODE[0])

def from_base4(string: str) -> int:
    value = 0

    for i, char in enumerate(reversed(string)):
        value += REVERSED_CODE[char] * (4 ** i)
    
    return value

def base4_sum(string: str) -> int:
    result = 0

    for char in string:
        result += CODE.get(char, 0)
    
    return result