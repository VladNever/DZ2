import copy # специальная утилита для "глубокого" копирования (всей структуры)
from decimal import Decimal, ROUND_HALF_UP
def new_window ():
    print("_" * 100)
def generator_id (inp):
    if inp == "1":
        return 1
    return 0
def main_menu_options ():
    print("Главное меню: \n"\
          "1 Ввод нового пользователя \n"\
          "2 Просмотр пользователей \n"\
          "q Выход")
    option = input("Введите номер операции (1, 2, q): ")
    if option == "1":
        return "1"
    elif option == "2":
        return "2"
    elif option == "q":
        return "q"
    else:
        new_window ()
        print("Проверьте вводимое значение")
def selecting_users_options():
    new_window ()
    print("Меню выбора пользователей: \n"
        "1 Просмотр информации по всем пользователям \n"\
        "2 Просмотр информации по одному пользователю")
    option = input("Введите номер операции (1, 2): ")
    if option == "1":
        return "1"
    if option == "2":
        return "2"
def get_all_user(inp, users_storage):
    if inp == "1":
        for key in users_storage:
            all_users = "Уникальный номер: {0} | Пользователь: {1} | Масса тела: {2} | Рост: {3} | Возраст: {4} | "\
                        "Индекс массы тела: {5} | Шкала: {6}".format(key, users_storage[key]["user_name"],
                                            users_storage[key]["user_weight"], users_storage[key]["user_height"],
                                            users_storage[key]["user_age"], users_storage[key]["user_bmi"],
                                            users_storage[key]["user_bmi_scale"])
            print(all_users)
    else:
        pass
def get_one_user(inp, users_storage):
    if inp == "2":
        selected_key = int(input("Введите уникальный номер пользователя: "))
        new_window ()
        if selected_key in users_storage:
            user = "Уникальный номер: {0} | Пользователь: {1} | Масса тела: {2} | Рост: {3} | Возраст: {4} | "\
                        "Индекс массы тела: {5} | Шкала: {6}".format(selected_key, users_storage[selected_key]["user_name"],
                                            users_storage[selected_key]["user_weight"], users_storage[selected_key]["user_height"],
                                            users_storage[selected_key]["user_age"], users_storage[selected_key]["user_bmi"],
                                            users_storage[selected_key]["user_bmi_scale"])
            print(user)
        else:
            print("Пользователь не найден")
    else:
        pass
def bmi_calculating (user_weight, user_height):
    user_bmi = Decimal(user_weight / user_height ** 2).quantize(Decimal("1"), rounding = ROUND_HALF_UP)
    return user_bmi
def bmi_scale_drawing (bmi):
    user_bmi = int(bmi)
    if user_bmi < 20:
        user_bmi_scale = ("20" + "|" + "=" * 30 + "50")
    elif user_bmi > 50:
        user_bmi_scale = ("20" + "=" * 30 + "|" + "50")
    else:
        user_bmi_scale = ("20" + "=" * (user_bmi - 20) + "|" + "=" * (30 - (user_bmi - 20)) + "50")
    return user_bmi_scale
def get_new_user (user_name, user_weight, user_height, user_age, user_bmi, user_bmi_scale, user_id):
    new_user = "Создан новый пользователь. \n"\
                    "Фамилия Имя Отчетсво: {0}\n"\
                    "Масса тела: {1}\n"\
                    "Рост: {2}\n"\
                    "Возраст: {3}\n"\
                    "Индекс массы тела: {4}\n"\
                    "Шкала индекса массы тела: {5}\n"\
                    "Уникальный номер: {6}".format(user_name, user_weight, user_height,
                                                user_age, user_bmi, user_bmi_scale, user_id)
    print(new_user)   
def creating_user (inp, current_id, users_storage):
    if inp == "1":
        new_window ()
        user = {}
        user["user_name"] = input("Введите вашу Фамилию Имя Отчество: ")
        user["user_weight"] = Decimal(input("Введите вашу массу тела в килограммах: "))
        user["user_height"] = Decimal(input("Введите ваш рост в метрах: "))
        user["user_age"] = int(input("Введите ваш возраст: "))
        user["user_bmi"] = bmi_calculating(user["user_weight"], user["user_height"])
        user["user_bmi_scale"] = bmi_scale_drawing(user["user_bmi"])
        user_id = current_id
        new_window()
        get_new_user(user["user_name"], user["user_weight"], user["user_height"], user["user_age"],
                        user["user_bmi"], user["user_bmi_scale"], user_id)
        # глубокое копирование данных
        users_storage[copy.deepcopy(user_id)] = copy.deepcopy(user)
        return users_storage
    else:
        return users_storage
def selecting_users(inp, users_storage):
    if inp == "2":
        option = selecting_users_options()
        new_window()
        get_all_user(option, users_storage)
        get_one_user(option, users_storage)
    else:
        pass
def main ():
    users_storage = {}
    current_id = 0
    while True:
        new_window()
        option = main_menu_options()
        if option == "q":
            break 
        current_id += generator_id(option)
        users_storage = creating_user(option, current_id, users_storage)
        selecting_users(option, users_storage)
main()