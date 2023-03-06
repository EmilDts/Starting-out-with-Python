line = str(input("Введите вашу строку: \n"))

# The program converts the term to lowercase:
lower_one = line.lower()

# The program asks the user what word he wants to replace:
line_old = str(input('Какое слово вы хотите заменить?: '))

# The program converts the term to lowercase:
lowe_two = line_old.lower()

position = lower_one.find(lowe_two)

# The program reports on which index of terms the word is present:
print(f'{lowe_two} находится на позиции: {position}')

# The program asks what word to replace:
line_new = str(input("Слово для замены: "))

# The program converts the term to lowercase:
lower_three = line_new.lower()

# Replacement:
line_replace = lower_one.replace(lowe_two, lower_three)

# The program removes the following punctuation marks from a string: ".,-:;?!"
crutch_one = line_replace.replace('.', ' ').replace(',', ' ').replace('-', ' ').replace(':', ' ')
crutch_two = crutch_one.replace(';', ' ').replace('?', ' ').replace('!', ' ')

print(crutch_two.strip())
