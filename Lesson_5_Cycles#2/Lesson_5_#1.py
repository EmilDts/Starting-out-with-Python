ere_we_go = float(input("Введите числа для подсчета. Когда закончите, то введите ключевое слово 'sum'. \n"))

memory = []

while True:
    while type(ere_we_go) == float:
        try:
            memory.append(ere_we_go)
            ere_we_go = float(input("Еще: \n"))
        except ValueError:
            print(exit(sum(memory)))
