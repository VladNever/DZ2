from decimal import Decimal, ROUND_HALF_UP
user_weight = Decimal(input("Введите Вашу массу тела в килограммах: "))
user_height = Decimal(input("Введите Ваш рост в метрах: "))
bmi = Decimal(user_weight / user_height ** 2).quantize(Decimal("1"), rounding = ROUND_HALF_UP)
print("Ваш индекс массы тела: ", bmi)
bmi = int(bmi) 
if bmi < 20:
    print("20" + "|" + "=" * 30 + "50")
elif bmi > 50:
    print("20" + "=" * 30 + "|" + "50")
else:
    print("20" + "=" * (bmi - 20) + "|" + "=" * (30 - (bmi - 20)) + "50")



