import math

# Exercise 1
# Hard way:
radians = float(input("Введите градусы для конвертации в радианы: "))
degrees = float(input("Введите радианы для конвертации в градусы: "))

radians_calculate = (radians * math.pi) / 180
degrees_calculate = (degrees * 180) / math.pi

print("Hard way")
print(f'Ваш ответ в радианах: {radians_calculate:.5f}; Ваш ответ в градусах: {degrees_calculate:.5f};')

# Easy way:
print("Easy way:")
print(f'Ваш ответ в радианах: {math.radians(radians):.5f}; Ваш ответ в градусах: {math.degrees(degrees):.5f};')
