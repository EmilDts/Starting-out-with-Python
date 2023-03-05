line = str(input("Введите вашу строку: \n"))

line_replace = str(input('Какое слово вы хотите заменить?: '))
position = line.find(line_replace)

print(f'{line_replace} находится на позиции {position}')
line_new = str(input("Слово для замены: "))

form = line.replace(line_replace, line_new)

form_strip = form.strip('.,-:;?!')

form_lower = form_strip.lower()

print(form_lower.lstrip())
