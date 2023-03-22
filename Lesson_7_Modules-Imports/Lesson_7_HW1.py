# Importing the 'math' library for our task:
import math


# Create a function to convert degrees to radians:
def radians_conversion():
    while True:
        try:
            radians = input()
            return math.radians(float(radians))
        except ValueError:
            print("Вы ввели не градусы! ")


# Create a function to convert radians to degrees:
def degrees_conversion():
    while True:
        try:
            degrees = input()
            return math.degrees(float(degrees))
        except ValueError:
            print("Вы ввели не радианы! ")


# An unnecessary part of the code that will not be executed when calling the functions above:
if __name__ == '__main__':

    print("""Привет!
Это программа для преобразования.
Если ты хочешь переобразовать радианы в градусы, то напиши 'радианы'.
Если ты хочешь переобразовать градусы в радианы, то напиши 'градусы'.""")

    # The user enters a value that, when tested for a specific result, returns the value to the function:
    renpy = str(input()).lower()

    while True:
        while renpy == "радианы":
            print(radians_conversion())
            exit()
        else:
            while renpy == "градусы":
                print(degrees_conversion())
                exit()
            else:
                print("Выбери из списка!")
                renpy = str(input()).lower()
