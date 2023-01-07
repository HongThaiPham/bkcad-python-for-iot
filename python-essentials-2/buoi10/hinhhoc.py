PI = 3.14


def ValidateCanh(a, b):
    '''validate gia tri canh'''
    if (a < 0 or b < 0):
        raise Exception("Phai la so duong")


def ChuViHinhChuNhat(a, b) -> float:
    '''ham tinh chu vi hinh chu nhat'''
    ValidateCanh(a, b)
    return (a+b)*2


def DienTichHinhChuNhat(a, b) -> float:
    '''ham tinh dien tich hinh chu nhat'''
    ValidateCanh(a, b)
    return a*b
