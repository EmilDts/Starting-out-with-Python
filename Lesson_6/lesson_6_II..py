line = str(input("Введите вашу строку: \n"))

order = list(line)

while "(" in order:
    passport = order.index("(")
    while order[passport] != ")":
        order.pop(passport)
    order.remove(")")
    if order[passport-1] == " ":
        order.pop(passport-1)
print(''.join(order))