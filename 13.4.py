try:
    i = int(input("Введите число:\t"))
    print("Вы ввели правильные числа")
except ValueError as e:
    print("Вы ввели неправильное число")
else:
    print(f"Вы ввели {i}")
finally:
    print("Выход из программы")
