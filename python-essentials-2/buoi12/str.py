def convertString(s, mode="upper|lower"):
    result = ''
    for c in s:
        # print(c, ord(c))
        if mode == "upper" and ord(c) >= 97 and ord(c) <= 122:
            result += chr(ord(c)-32)
        elif mode == "lower" and ord(c) < 97 and ord(c) >= 65:
            result += chr(ord(c)+32)
        else:
            result += c
    print(result)
    return result


convertString("123ABCdef", 'lower')
convertString("helloWorld", 'upper')
convertString("helloABC13world", 'lower')
