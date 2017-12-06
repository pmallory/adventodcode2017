def square_poo(limit=500000):
    i = 1
    while (i+1)**2 < limit:
        yield i**2, i-1
        i += 2

def locate_num(n):
    cns = square_poo()
    corner_num, side_length = next(cns)
    while True:
        if corner_num >= n:
            break
        corner_num, side_length = next(cns)

    if corner_num-side_length < n <= corner_num:
        dp = corner_num-n-(side_length//2)
    elif corner_num-(2*side_length) < n <= corner_num-side_length:
        dp = corner_num-n-(side_length//2)-side_length
    elif corner_num-(3*side_length) < n <= corner_num-(2*side_length):
        dp = corner_num-n-(side_length//2)-2*side_length
    else:
        dp = corner_num-n-(side_length//2)-3*side_length

    return (side_length//2, abs(dp))
