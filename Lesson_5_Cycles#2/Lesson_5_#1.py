# Asking the user to enter numbers:
ere_we_go = float(input("Введите числа для подсчета. Когда закончите, то введите ключевое слово 'sum'. \n"))

# We create a list in which we will store user values:
memory = []

while True:

    # Compare user value for data type identity:
    while type(ere_we_go) == float:

        # If everything is OK, then add the value to the list, and ask you to enter the value again:
        try:
            memory.append(ere_we_go)
            ere_we_go = float(input("Еще: \n"))

        # If not OK, then the program performs the operation on error and reads the value in the "memory" list:
        except ValueError:
            print(exit(sum(memory)))
