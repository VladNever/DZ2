text1 = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"
print("Количество символов: ", len(text1))
print("Инверсная строка: ", text1[::-1])
print("Каждое слово с большой буквы: ", text1.title())
print("Весь текст прописными: ", text1.upper())
print("Число вхождений \"нд\" = {0}, \"ам\" = {1}".format(text1.count("нд"), text1.count("ам")))
print("\"нд\" больше чем \"ор\": ", text1.count("нд") > text1.count("ор"))
print(text1)
print("Смена регистра: ", text1.swapcase())
print("Не\nзнаю,\nкак\nтам\nв\nЛондоне,\nя\nне\nбыла.\nМожет,\nтам\nсобака\n—\nдруг\nчеловека.\nА\nу\nнас\nуправдом\n—\nдруг\nчеловека!")

print("Привет!")