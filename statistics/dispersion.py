def num_input():
    values = []
    x = int(input())
    while x != 0:
        values.append(x)
        x = int(input())
    return values

def arifmetic_mean(numbers):
    return sum(numbers) / len(numbers)

def dispersion(numbers, is_generis):
    amount = 0
    mean = arifmetic_mean(numbers)
    for number in numbers:
        amount += (mean - number)**2
    if is_generis:
        return amount / len(numbers)
    else:
        return amount / (len(numbers) - 1)

def standart_deviation(numbers, is_generis):
    return dispersion(numbers, is_generis)**0.5

def find_range(numbers):
    numbers = sorted(numbers)
    return numbers[len(numbers)-1] - numbers[0]

def find_median(numbers):
    numbers = sorted(numbers)
    print(numbers)
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers)//2 - 1] + numbers[len(numbers)//2]) / 2
    else:
        return numbers[len(numbers)//2]

arr = num_input()

print("Среднее арифметическое: " + str(arifmetic_mean(arr)))
print("Дисперсия: " + str(dispersion(arr, False)))
print("Стандартное отклонение: " + str(standart_deviation(arr, False)))
print("Размах: " + str(find_range(arr)))
print("Медиана: " + str(find_median(arr)))