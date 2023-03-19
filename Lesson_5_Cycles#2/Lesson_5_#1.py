line = float(input("Введите числа для подсчета. Когда закончите, то введите ключевое слово 'sum'. \n"))

memory = []

while True:
    while type(line) == float:
        try:
            memory.append(line)
            line = float(input("Еще: \n"))
        except ValueError:
            print(sum(memory))
            exit()

