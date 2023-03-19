import math


def radians_conversion():
    while True:
        try:
            radians = input()
            return math.radians(float(radians))
        except ValueError:
            print("Вы ввели не градусы! ")


def degrees_conversion():
    while True:
        try:
            degrees = input()
            return math.degrees(float(degrees))
        except ValueError:
            print("Вы ввели не радианы! ")


if __name__ == '__main__':
    print("""
    Привет!\n
    Это программа для преобразования.\n
    Если ты хочешь переобразовать радианы в градусы, то напиши 'радианы'.\n.
    Если ты хочешь переобразовать градусы в радианы, то напиши 'градусы'.\n
    """)

    renpy = str(input()).lower()

    while not renpy == "радианы" or renpy == "градусы":
        print("Выбери из списка!")
        renpy = input().lower()
    else:
        if renpy == "радианы":
            print(radians_conversion())
        else:
            print(degrees_conversion())
