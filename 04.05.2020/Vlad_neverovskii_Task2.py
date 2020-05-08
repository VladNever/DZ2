import copy # специальная утилита для "глубокого" копирования (всей структуры)
from decimal import Decimal, ROUND_HALF_UP
users_dic = {}
generator_id = 0
while True:
    print("_" * 100)
    print("1 Ввод нового пользователя \n"\
          "2 Просмотр пользователей \n"\
          "q Выход")
    option_selection = input("Введите номер операции (1, 2, q): ") 
    print("_" * 100)
    if option_selection == "1":
        generator_id += 1
        user = {}
        user["user_name"] = input("Введите вашу Фамилию Имя Отчество: ")
        user["user_weight"] = Decimal(input("Введите вашу массу тела в килограммах: "))
        user["user_height"] = Decimal(input("Введите ваш рост в метрах: "))
        user["user_age"] = int(input("Введите ваш возраст: "))
        print("_" * 100)
        user_bmi = Decimal(user["user_weight"] / user["user_height"] ** 2).quantize(Decimal("1"), rounding = ROUND_HALF_UP)
        user["user_bmi"] = user_bmi
        user_bmi = int(user_bmi) 
        if user_bmi < 20:
            user_bmi_scale = ("20" + "|" + "=" * 30 + "50")
        elif user_bmi > 50:
            user_bmi_scale = ("20" + "=" * 30 + "|" + "50")
        else:
            user_bmi_scale = ("20" + "=" * (user_bmi - 20) + "|" + "=" * (30 - (user_bmi - 20)) + "50")
        user["user_bmi_scale"] = user_bmi_scale
        user_id = generator_id
        new_user_result = "Пользователь: {0}\n"\
              "Масса тела: {1}\n"\
              "Рост: {2}\n"\
              "Возраст: {3}\n"\
              "Индекс массы тела: {4}\n"\
              "Шкала индекса массы тела: {5}\n"\
              "Уникальный номер: {6}".format(user["user_name"], user["user_weight"], user["user_height"],
                                                   user["user_age"], user["user_bmi"], user["user_bmi_scale"], user_id)
        print(new_user_result)
        # глубокое копирование данных
        users_dic[copy.deepcopy(user_id)] = copy.deepcopy(user)
        # очистка переменной. А надо ли?
        user = 0
    elif option_selection == "2":
        print("1 Просмотр информации по всем пользователям \n"\
              "2 Просмотр информации по одному пользователю")
        option_selection_choise = input("Введите номер операции (1, 2): ")
        if option_selection_choise == "1":
            for key in users_dic:
                selection_1 = "Уникальный номер: {0} | Пользователь: {1} | Масса тела: {2} | Рост: {3} | Возраст: {4} |"\
                              "Индекс массы тела: {5} | Шкала: {6}".format(key, users_dic[key]["user_name"],
                                                   users_dic[key]["user_weight"], users_dic[key]["user_height"],
                                                   users_dic[key]["user_age"], users_dic[key]["user_bmi"],
                                                   users_dic[key]["user_bmi_scale"])
                print(selection_1)
        if option_selection_choise == "2":
            selected_key = int(input("Введите уникальный номер пользователя: "))
            if selected_key in users_dic:
                selection_2 = "Уникальный номер: {0} | Пользователь: {1} | Масса тела: {2} | Рост: {3} | Возраст: {4} |"\
                              "Индекс массы тела: {5} | Шкала: {6}".format(selected_key, users_dic[selected_key]["user_name"],
                                                   users_dic[selected_key]["user_weight"], users_dic[selected_key]["user_height"],
                                                   users_dic[selected_key]["user_age"], users_dic[selected_key]["user_bmi"],
                                                   users_dic[selected_key]["user_bmi_scale"])
                print(selection_2)
            else:
                print("Пользователь не найден")
    elif option_selection == "q":
        break
    else:
        print("Проверьте вводимое значение")