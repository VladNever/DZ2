num_1 = int(input("Введите число 1: "))
num_2 = int(input("Введите число 2: "))
num_3 = int(input("Введите число 3: "))
no_zero_numbers = num_1 and num_2 and num_3 and print("Нет нулевых значений!!!")
first_pos_number = num_1 or num_2 or num_3 or "Введены все нули!"
print(first_pos_number)
if num_1 > (num_2 + num_3):
    print("a - b - c")
if num_1 < (num_2 + num_3):
    print("b + c - a")
if num_1 > 50 and (num_2 > num_1 or num_3 > num_1):
    print("Вася")
if num_1 > 5 or (num_2 == 7 and num_3 == 7):
    print("Петя")