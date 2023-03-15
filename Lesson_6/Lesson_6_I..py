line = str(input("Введите вашу строку: ")).strip("!;?:,.() \n\t").lower()

while not line == list[::-1]:
    print(f'Строка "{line.capitalize()}" не является палиндромом "{line[::-1].capitalize()}"')
    line = str(input("Введите вашу строку: ")).strip("!;?:,.()").lower()
else:
    print(f'Строка "{line.capitalize()}" является палиндромом "{line[::-1].capitalize()}"')
