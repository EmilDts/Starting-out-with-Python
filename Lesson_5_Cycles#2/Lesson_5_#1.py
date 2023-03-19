line = float(input("Введите числа для подсчета. Когда закончите, то введите ключевое слово 'sum'. \n"))

memory = []

while type(line) == float:
    memory.append(line)
    line = float(input("Еще: \n"))
else:
    if line == "sum":
        print(sum(memory))
    else:
        print("Некорректный ввод")