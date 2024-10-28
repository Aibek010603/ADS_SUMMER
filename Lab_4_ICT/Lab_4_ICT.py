# Задание 1: Калькулятор с условными операторами
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Ошибка: Деление на ноль невозможно."
else:
    result = "Ошибка: Неверная операция."

print("Результат:", result)


# Задание 2: Калькулятор с циклом
while True:
    num1 = input("Введите первое число (или 'q' для выхода): ")
    if num1.lower() == 'q':
        break
    num1 = float(num1)
    
    num2 = float(input("Введите второе число: "))
    operation = input("Введите операцию (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Ошибка: Деление на ноль невозможно.")
            continue
    else:
        print("Ошибка: Неверная операция.")
        continue

    print("Результат:", result)



# Задание 3: Вывод чисел от 1 до 20
for i in range(1, 21):
    print(i)




# Задание 4: Квадрат каждого числа в списке
numbers = list(range(1, 11))
for num in numbers:
    print(num ** 2)



# Задание 5: Генерация всех комбинаций бутербродов
bread = ["белый", "черный"]
meat = ["курица", "индейка", "говядина"]
vegetables = ["салат", "помидор", "огурец"]
sauces = ["майонез", "чесночный", "кетчуп"]

for b in bread:
    for m in meat:
        for v in vegetables:
            for s in sauces:
                print(f"Бутерброд с {b} хлебом, {m} мясом, {v} и соусом {s}.")
                
        
        
        
# Задание 6: Сумма чётных и нечётных чисел от 1 до 100
sum_even = 0
sum_odd = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print("Сумма чётных чисел:", sum_even)
print("Сумма нечётных чисел:", sum_odd)



# Задание 7: Вычисление факториала
num = int(input("Введите число для вычисления факториала: "))
factorial = 1

if num < 0:
    print("Факториал не определён для отрицательных чисел.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"Факториал числа {num} равен {factorial}.")





