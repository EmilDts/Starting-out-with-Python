list = str(input("Введите вашу строку: ")).strip("!;?:,.() \n\t").lower()

while not list == list[::-1]:
    print(f'Строка "{list.capitalize()}" не является палиндромом "{list[::-1].capitalize()}"')
    list = str(input("Введите вашу строку: ")).strip("!;?:,.()").lower()
else:
    print(f'Строка "{list.capitalize()}" является палиндромом "{list[::-1].capitalize()}"')