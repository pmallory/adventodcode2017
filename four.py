import sys

def count(passphrase_list):
    c = 0
    for line in passphrase_list:
        words = line.split()
        words = [''.join(sorted(w)) for w in words]
        if len(words) == len(set(words)):
            c += 1
    return c



print(count(sys.stdin.readlines()))
