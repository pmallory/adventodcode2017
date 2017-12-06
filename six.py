from itertools import cycle

def reallocate(banks):
    seen_before = set()

    max_idx = banks.index(max(banks))
    num2distribubte = banks[max_idx]

    banks[max_idx] = 0

    iterator = cycle(range(len(banks)))

    while next(iterator) != max_idx:
        continue

    while num2distribubte > 0:
        banks[next(iterator)] += 1
        num2distribubte -= 1

    return banks


def count_cycles(banks):
    count = 1
    seen_before = {tuple(banks): 1}

    while True:
        banks = reallocate(banks)
        tb = tuple(banks)
        if tb in seen_before:
            return count - seen_before[tb]

        seen_before[tb] = count
        count += 1
