numbers = input("Введите числа для подсчета. Когда закончите, то введите ключевое слово 'sum'. \n").lower()

memory = []

while isinstance(numbers, int) or isinstance(numbers, float) :
    memory.append(numbers)
    numbers = input("Еще \n").lower()
else:
    if numbers != "sum":
        print("Некорректный ввод")
    else:
        print(sum(memory))