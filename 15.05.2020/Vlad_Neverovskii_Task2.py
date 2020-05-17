import datetime
# Модуль для работы с регулярными выражениями
import re
def main():
    import os, datetime
    # os.path.dirname(path) - возвращает имя директории пути path.
    PROJECT_DIR = os.path.dirname(__file__)
    DB_FILE = os.path.join(PROJECT_DIR, "11.05.2020.txt")
    fp = open(DB_FILE, "r")
    request_counter = 0
    safari_counter = 0
    firefox_counter = 0
    ip_list = list()
    global_adjusted_list = list()
    date_filter = dict()
    # цикл перебирает файл по-строчно:
    for main_string in fp:

        # Разбор строки по нескольким сложным разделителям
        # делается через регулярные выражения.  
        # re.escape(pattern) - решает вопрос со спец. символами в строке
        # map(func, *iterables) - создаёт итератор, который вычисляет функцию,
        # используя аргументы каждого из итераций. Останавливается,
        # когда самая короткая итерация исчерпана.
        # join(self, iterable, /) - объединяет любое количетсво строк, используя разделитель
        # re.split(pattern, string, maxsplit=0, flags=0) - разбивает исходную строку по вхождению шаблона, 
        # возвращая список, содержащий результирующие подстроки. Если в шаблоне используются захватывающие
        # скобки, то текст всех групп в шаблоне также возвращается как часть результирующего списка. Если 
        # maxsplit не равен нулю, происходит максимальное расщепление maxsplit, а остаток строки возвращается 
        # как последний элемент списка.

        # Определение разделителей:
        delimiters = ' - -', ' [', '] ', '"'
        # Создание паттерна:
        regexPattern = '|'.join(map(re.escape, delimiters))
        # Разделение строки:
        elements_list = re.split(regexPattern, main_string)
        elements_list[2] = (datetime.datetime.strptime(elements_list[2],
                            '%d/%B/%Y:%H:%M:%S %z')).date().strftime("%Y.%m.%d")
        adjusted_list = []
        adjusted_list.append(elements_list[0])
        adjusted_list.append(elements_list[2])
        if "Safari" in elements_list[8]:
            adjusted_list.append("Safari")
            safari_counter += 1
        else:
            adjusted_list.append("-")
        if "Firefox" in elements_list[8]:
            adjusted_list.append("Firefox")
            firefox_counter += 1
        else:
            adjusted_list.append("-")
        global_adjusted_list.append(adjusted_list)
        request_counter += 1
        ip_list.append(elements_list[0])
    for lst in global_adjusted_list:
        if lst[1] in date_filter:
            date_filter[lst[1]][0].append(lst[0])
            date_filter[lst[1]][1].add(lst[0])
            date_filter[lst[1]][2].append(lst[2])
            date_filter[lst[1]][3].append(lst[3])
        else:
            date_filter[lst[1]] = [[lst[0]], {lst[0]}, [lst[2]], [lst[3]]]
    for dt in date_filter:
        date_index = dt
        all_ip = len(date_filter[dt][0])
        unique_ip = len(date_filter[dt][1])
        Safari_brw = date_filter[dt][2].count("Safari")
        Firefox_brw = date_filter[dt][3].count("Firefox")
        print(f"{date_index} Всего запросов/IP: {all_ip}, уникальных IP: {unique_ip}, "\
              f"Safari: {Safari_brw}, Firefox: {Firefox_brw}")
    print(f"Всего запросов/IP: {request_counter}, уникальных IP: {len(list(set(ip_list)))}, "\
        f"Safari: {safari_counter}, Firefox: {firefox_counter}")
    fp.close()
main()