import statistics
import math

x = int(input())
values = []
squares_amount = 0
amount = 0

while x != 0:
    amount += x
    values.append(x)
    x = int(input())

mean = amount / len(values)

for value in values:
    squares_amount += (mean - value)**2

dispersion = squares_amount / (len(values))
standart_deviation = dispersion**0.5

print("Среднее арифметическое: " + str(mean))
print("Дисперсия: " + str(dispersion))
print("Стандартное отклонение: " + str(standart_deviation))

print("По библиотеке sd: " + str(math.sqrt(statistics.variance(values))))