import sys

s = sys.stdin.readlines()

program = []

for line in s:
    program.append(int(line))

count = 0
ptr = 0

while True:
    jump_distance = program[ptr]
    if jump_distance >= 3:
        program[ptr] -= 1
    else:
        program[ptr] += 1
    ptr += jump_distance
    count += 1

    if ptr < 0 or ptr >= len(program):
        break

print(count)
