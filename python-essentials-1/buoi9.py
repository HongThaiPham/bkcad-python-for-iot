
# Bai 1
# nhap 2 so nguyen, in ra tong hieu tich thuong
# co the nhap so, chuoi
# viet bang function

# def validateInput(a):
#     if type(x) != int:


def tong(*agr):
    sum = 0
    for i in agr:
        sum += i
    print("Tong: {}".format(sum))


def hieu(*agr):
    h = agr[0]
    for i in range(1, len(agr)):
        h -= i
    print("Hieu: {}".format(h))


def tich(*agr):
    h = agr[0]
    for i in range(1, len(agr)):
        h -= i
    print("Hieu: {}".format(h))


def thuong(*agr):
    h = agr[0]
    for i in range(1, len(agr)):
        h -= i
    print("Hieu: {}".format(h))


def Bai1():
    try:
        a, b = map(int, input("a, b: ").split(","))
        tong(a, b)
        hieu(a, b)
    except ValueError:
        print("Nhap sai dinh dang")
    except Exception as e:
        print(e)


# Bai1()
# Bai 2
# dinh nghia exception ten laf SoDuongException
# nhap vao so tien bat ky, la so duong,
# neu < 0  thi quang exception noi dung "So vua nhap phai lon hon 0"
# x = 'xx'
# print(type(x) == int)

class SoDuongException(Exception):
    ''' check so duong'''

    def __init__(self):
        super().__init__("So vua nhap phai lon hon 0")
    pass


def Bai2():
    try:
        a = int(input("a: "))
        if (a <= 0):
            raise SoDuongException
        print("So a: {}".format(a))
    except Exception as e:
        print(e)


Bai2()
