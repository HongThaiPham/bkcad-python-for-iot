pattern = ['1111110', '0110000', '1101101', '1111001', '0110011',
           '1011011', '1011111', '1110000', '1111111', '1111011']


def led_display(input_num='0123456789', ch='#'):
    if (not input_num.isdigit()):
        return None

    lines = ['' for _ in range(5)]
    print(lines)
    for n in input_num:
        segment = [['', '', ''] for _ in range(5)]
        current_num = int(n)
        current_num_pattern = pattern[current_num]
        if current_num_pattern[0] == '1':
            segment[0][0] = segment[0][1] = segment[0][2] = ch
        if current_num_pattern[1] == '1':
            segment[0][2] = segment[1][2] = segment[2][2] = ch
        if current_num_pattern[2] == '1':
            segment[2][2] = segment[3][2] = segment[4][2] = ch
        if current_num_pattern[3] == '1':
            segment[4][0] = segment[4][1] = segment[4][2] = ch
        if current_num_pattern[4] == '1':
            segment[2][0] = segment[3][0] = segment[4][0] = ch
        if current_num_pattern[5] == '1':
            segment[0][0] = segment[1][0] = segment[2][0] = ch
        if current_num_pattern[6] == '1':
            segment[2][0] = segment[2][1] = segment[2][2] = ch
        for line in range(5):
            lines[line] += ''.join(segment[line]) + ' '
        print(segment)
    for l in lines:
        print(l)


def print_pattern():
    for r in pattern:
        for c in r:
            if c == '':
                print(' ', end='')
            print(c, end=' ')
        print('\n')


led_display()
