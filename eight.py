import sys
from collections import defaultdict

def tokenize(line):
    tokens = line.split()

    operand = tokens[0]

    operation = tokens[1]

    arg = int(tokens[2])

    comparison_reg = tokens[4]

    if tokens[5] == '<':
        comparison_op = int.__lt__
    elif tokens[5] == '>':
        comparison_op = int.__gt__
    elif tokens[5] == '>=':
        comparison_op = int.__ge__
    elif tokens[5] == '<=':
        comparison_op = int.__le__
    elif tokens[5] == '==':
        comparison_op = int.__eq__
    elif tokens[5] == '!=':
        comparison_op = lambda x,y: x != y

    comparison_arg = int(tokens[6])

    return operand, operation, arg, comparison_reg, comparison_op, comparison_arg

memory = defaultdict(int)
max_seen = 0

for line in sys.stdin.readlines():
    operand, operation, arg, comparison_reg, comparison_op, comparison_arg = tokenize(line)
    if comparison_op(memory[comparison_reg], comparison_arg):
        if operation == 'inc':
            memory[operand] += arg
        elif operation == 'dec':
            memory[operand] -= arg

    if memory[operand] > max_seen:
        max_seen = memory[operand]

print(max(memory.values()))
print(max_seen)
