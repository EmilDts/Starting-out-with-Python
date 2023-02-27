# Exercise 2
first_counter_data = float(input("Введите показания первого счетчика: "))
second_counter_data = float(input("Введите показания второго счетчика: "))
rate = float(input("Введите тариф: "))

calculation = (first_counter_data - second_counter_data) * rate

print(f'Оплата будет составлять {calculation:.2f} за использования {first_counter_data} кВт*ч электроэнергии.')
