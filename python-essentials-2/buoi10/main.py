import hinhhoc
# import sound
import calculator.app


def HinhChuNhat():
    try:
        a, b = map(float, input("Nhap dai, rong: ").split(','))

        chuvi = hinhhoc.ChuViHinhChuNhat(a, b)
        dientich = hinhhoc.DienTichHinhChuNhat(a, b)

        print("Chu vi: {}".format(chuvi))
        print("Dien tich: {}".format(dientich))

    except ValueError:
        print("Gia tri khong phu hop")
    except Exception as e:
        print(e)


def main():
    # HinhChuNhat()
    calculator.app.main()


main()
