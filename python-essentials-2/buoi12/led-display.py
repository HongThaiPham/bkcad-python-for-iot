pattern = [['#', '#', '#'], ['#', '', '#'], [
    '#', '#', '#'], ['#', '', '#'], ['#', '#', '#']]


def led_display(input_num='8123'):
    if (not input_num.isdigit()):
        return None

    for n in input_num:
        if (n == '8'):
            print_pattern()


def print_pattern():
    for r in pattern:
        for c in r:
            if c == '':
                print(' ', end='')
            print(c, end=' ')
        print('\n')


led_display()
