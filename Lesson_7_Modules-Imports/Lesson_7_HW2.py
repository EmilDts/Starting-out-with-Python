import math


def does_it_exist():
    if a + b > c:
        return True
    elif a + c > b:
        return True
    elif b + c > a:
        return True
    else:
        return False


def perimeter():
    p = a + b + c
    return float(p)


def area():
    while True:
        try:
            semi_p = perimeter() / 2
            s = math.sqrt(semi_p * (semi_p - a) * (semi_p - b) * (semi_p - c))
            return float(s)
        except ValueError:
            exit(print("Немыслимо..."))


if __name__ == '__main__':
    print("Привет, это программа для расчета треугольника!")

    while True:
        try:
            a = abs(float(input("Введите сторону 'a': ")))
            break
        except ValueError:
            print("Некорректный ввод!")
            a = abs(float(input("Введите сторону 'a': ")))
    while True:
        try:
            b = abs(float(input("Введите сторону 'b': ")))
            break
        except ValueError:
            print("Некорректный ввод!")
            b = abs(float(input("Введите сторону 'b': ")))
    while True:
        try:
            c = abs(float(input("Введите сторону 'c': ")))
            break
        except ValueError:
            print("Некорректный ввод!")
            c = abs(float(input("Введите сторону 'c': ")))

    print("Исходя из данных, которые вы ввели, у вас получается следующие: \n")
    print(f"Треугольник существует? {does_it_exist()}\n Его периметр: {perimeter():.2f}\n Его площадь: {area():.2f}")
