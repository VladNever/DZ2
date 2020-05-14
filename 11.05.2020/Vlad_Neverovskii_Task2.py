def main():
    import os
    # os.path.dirname(path) - возвращает имя директории пути path.
    PROJECT_DIR = os.path.dirname(__file__)
    DB_FILE = os.path.join(PROJECT_DIR, "11.05.2020.txt")
    fp = open(DB_FILE, "r")
    request_counter = 0
    safari_counter = 0
    firefox_counter = 0
    ip_list = list()
    # цикл перебирает файл по-строчно:
    for line in fp:
        request_counter += 1
        ip, fnd_browser = line.split(" - - ")
        splited = fnd_browser.split("\"")
        ip_list.append(ip)
        if "Safari" in splited[5]:
            safari_counter += 1
            pass
        if "Firefox" in splited[5]:
            firefox_counter += 1
            pass
    print(f"Количество запросов: {request_counter}")
    print(f"Количество уникальных ip адресов: {len(list(set(ip_list)))}")
    print(f"Количество запросов с использованием браузера Safari: {safari_counter}")
    print(f"Количество запросов с использованием браузера Firefox: {firefox_counter}")
    fp.close()
main()