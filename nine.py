import sys

stream = sys.stdin.read()
cp = 0
depth = 0
score = 0
garbagecount = 0

ingarbage = False

while cp < len(stream):
    char = stream[cp]

    if ingarbage:
        if char == '!':
            cp += 1
        elif char == '>':
            ingarbage = False
        else:
            garbagecount += 1
    else:
        if char == '{':
            depth += 1
        elif char == '}':
            score += depth
            depth -= 1
        elif char == '<':
            ingarbage = True


    cp += 1


print(score)
print(garbagecount)
