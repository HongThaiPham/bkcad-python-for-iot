import utils.my_calculator


def menu():
    print("--- CALCULATOR ---")
    print("1. Phep cong")
    print("2. Phep tru")
    print("3. Phep nhan")
    print("4. Phep chia")
    print("5. Phep sin")
    print("6. Phep cos")
    print("7. Thoat")


def main():
    menu()
    user_select = int(input("Chon chuc nang: "))
    while (user_select < 7):
        if user_select == 1:
            so = tuple(
                map(int, input("Nhap so cach nhay boi dau ,: ").split(',')))
            print("Tong: {}".format(utils.my_calculator.add(so)))
        if user_select == 2:
            a, b = map(int, input("Nhap 2 so cach nhay boi dau ,: ").split(','))
            print("Hieu: {}".format(utils.my_calculator.sub(a, b)))
        if user_select == 3:
            so = tuple(
                map(int, input("Nhap so cach nhay boi dau ,: ").split(',')))
            print("Tich: {}".format(utils.my_calculator.mul(so)))
        if user_select == 4:
            a, b = map(int, input("Nhap 2 so cach nhay boi dau ,: ").split(','))
            print("Thuong: {}".format(utils.my_calculator.div(a, b)))
        if user_select == 5:
            a = int(input("Nhap 1 so de tinh SIN ,: "))
            print("SIN: {}".format(utils.my_calculator.sin(a)))
        if user_select == 6:
            a = int(input("Nhap 1 so de tinh COS ,: "))
            print("COS: {}".format(utils.my_calculator.cos(a)))
        menu()
        user_select = int(input("Chon chuc nang: "))


main()
