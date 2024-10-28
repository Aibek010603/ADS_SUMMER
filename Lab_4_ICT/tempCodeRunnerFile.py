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
