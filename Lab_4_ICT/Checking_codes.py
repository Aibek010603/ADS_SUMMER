# Задание 7: Вычисление факториала
num = int(input("Введите число для вычисления факториала: "))
factorial = 1

if num < 0:
    print("Факториал не определён для отрицательных чисел.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"Факториал числа {num} равен {factorial}.")
