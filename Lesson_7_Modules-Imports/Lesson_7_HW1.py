import math

def radians_conversion(degrees: float):
    while True:
        try:
            radians = input(degrees)
            return math.radians(float(radians))
        except ValueError:
            print("Вы ввели не градусы! ")


def degrees_calculate(radians: float):
    while True:
        try:
            degrees = input(radians)
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

    renpy = input().lower()

    if renpy == "радианы":
        print(radians_conversion)
    elif renpy == "градусы":
        print(degrees_calculate)
    else:
        print("Выбери из списка!")
