import sys

s = sys.stdin.read().strip()

count = 0

for i in range(len(s)):
    if s[i] == s[(i+len(s)//2)%len(s)]:
        count += int(s[i])

print(count)
