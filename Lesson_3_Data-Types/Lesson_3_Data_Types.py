line = str(input("Введите вашу строку: \n"))
lower_one = line.lower()

line_old = str(input('Какое слово вы хотите заменить?: '))
lowe_two = line_old.lower()
position = lower_one.find(lowe_two)

print(f'{lowe_two} находится на позиции: {position}')

line_new = str(input("Слово для замены: "))
lower_three = line_new.lower()

line_replace = lower_one.replace(lowe_two, lower_three)

crutch_one = line_replace.replace('.', ' ').replace(',', ' ').replace('-', ' ').replace(':', ' ')
crutch_two = crutch_one.replace(';', ' ').replace('?', ' ').replace('!', ' ')

print(crutch_two.strip())