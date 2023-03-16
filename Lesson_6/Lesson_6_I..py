# The user enters a string:
line = str(input("Введите вашу строку: ")).strip("!;?:,.() \n\t").lower()

# If the user string is not equal to the back end string:
while not line == line[::-1]:

    # True is executed and the user is asked to enter the string again:
    print(f'Строка "{line.capitalize()}" не является палиндромом "{line[::-1].capitalize()}"')
    line = str(input("Введите вашу строку: ")).strip("!;?:,.()").lower()
else:
    print(f'Строка "{line.capitalize()}" является палиндромом "{line[::-1].capitalize()}"')
