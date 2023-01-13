def encryp_text(text, num=1):
    cipher = ''
    for char in text:
        if not char.isalpha():
            continue
        # char = char.upper()
        code = ord(char) + num
        if code > ord('Z'):
            code = ord('A')
        if code < ord('Z'):
            code = ord('A')
        cipher += chr(code)
    return cipher


def decrypt_cipher(cipher):
    text = ''
    for char in cipher:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) - 1
        if code < ord('A'):
            code = ord('Z')
        text += chr(code)
    return text


print(encryp_text("abcxyzABCxyz 123", 2))

print(ord('a'))
print(ord('z'))
print(ord('A'))
print(ord('Z'))
