def triangle(n):
    if n % 2 == 0:
        print("Ошибка! Число должно быть нечетным.")
        return

    for i in range(1, n):
        line = "*" * i
        print(line)
    for i in range(-n, 1 ):
        line = "*" * -i
        print(line)

n = int(input("Введите нечетное натуральное число: "))
triangle(n)