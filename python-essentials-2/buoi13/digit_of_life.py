def digit_of_life(inp):
    if len(inp) == 1:
        return int(inp)
    sum = 0
    # while (len(inp) > 1):
    #     sum = 0
    for d in inp:
        sum += int(d)
        # inp = str(sum)
    return digit_of_life(str(sum)) if len(str(sum)) > 1 else sum


print(digit_of_life('19991229'))
print(digit_of_life('20000101'))
