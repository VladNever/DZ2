import datetime
import os
import pytz
import time
class Happy_time:
    def __init__(self, time_parts):
        self.time_parts = time_parts
    def draw_number(self, num):
        if num == "0":
            s_1 = "█" * 8
            s_2 = "█" * 8
            s_3 = "█"*3 + "  " + "█"*3
            s_4 = "█"*3 + "  " + "█"*3
            s_5 = "█"*3 + "  " + "█"*3
            s_6 = "█"*3 + "  " + "█"*3
            s_7 = "█"*3 + "  " + "█"*3
            s_8 = "█"*3 + "  " + "█"*3
            s_9 = "█" * 8
            s_10 = "█" * 8
            return [s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8, s_9, s_10]
        elif num == "1":
            s_1 = "█" * 6 + "  "
            s_2 = "█" * 6 + "  "
            s_3 = "   " + "█" * 3 + "  "
            s_4 = "   " + "█" * 3 + "  "
            s_5 = "   " + "█" * 3 + "  "
            s_6 = "   " + "█" * 3 + "  "
            s_7 = "   " + "█" * 3 + "  "
            s_8 = "   " + "█" * 3 + "  "
            s_9 = "█" * 8
            s_10 = "█" * 8
            return [s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8, s_9, s_10]
        elif num == "2":
            s_1 = "█" * 8
            s_2 = "█" * 8
            s_3 = "     " + "█" * 3
            s_4 = "     " + "█" * 3
            s_5 = "█" * 8
            s_6 = "█" * 8
            s_7 = "█" * 3 + "     "
            s_8 = "█" * 3 + "     "
            s_9 = "█" * 8
            s_10 = "█" * 8
            return [s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8, s_9, s_10]
        elif num == "3":
            s_1 = "█" * 8
            s_2 = "█" * 8
            s_3 = "     " + "█" * 3
            s_4 = "     " + "█" * 3
            s_5 = "█" * 8
            s_6 = "█" * 8
            s_7 = "     " + "█" * 3
            s_8 = "     " + "█" * 3
            s_9 = "█" * 8
            s_10 = "█" * 8
            return [s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8, s_9, s_10]
        elif num == "4":
            s_1 = "█" * 3 + "  " + "█" * 3
            s_2 = "█" * 3 + "  " + "█" * 3
            s_3 = "█" * 3 + "  " + "█" * 3
            s_4 = "█" * 3 + "  " + "█" * 3
            s_5 = "█" * 8
            s_6 = "█" * 8
            s_7 = "     " + "█" * 3
            s_8 = "     " + "█" * 3
            s_9 = "     " + "█" * 3
            s_10 = "     " + "█" * 3
            return [s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8, s_9, s_10]
        elif num == "5":
            s_1 = "█" * 8
            s_2 = "█" * 8
            s_3 = "█" * 3 + "     "
            s_4 = "█" * 3 + "     "
            s_5 = "█" * 8
            s_6 = "█" * 8
            s_7 = "     " + "█" * 3
            s_8 = "     " + "█" * 3
            s_9 = "█" * 8
            s_10 = "█" * 8
            return [s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8, s_9, s_10]
        elif num == "6":
            s_1 = "█" * 3 + "     "
            s_2 = "█" * 3 + "     "
            s_3 = "█" * 3 + "     "
            s_4 = "█" * 3 + "     "
            s_5 = "█" * 8
            s_6 = "█" * 8
            s_7 = "█" * 3 + "  " + "█" * 3
            s_8 = "█" * 3 + "  " + "█" * 3
            s_9 = "█" * 8
            s_10 = "█" * 8
            return [s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8, s_9, s_10]
        elif num == "7":
            s_1 = "█" * 8
            s_2 = "█" * 8
            s_3 = "     " + "█" * 3
            s_4 = "     " + "█" * 3
            s_5 = "     " + "█" * 3
            s_6 = "     " + "█" * 3
            s_7 = "     " + "█" * 3
            s_8 = "     " + "█" * 3
            s_9 = "     " + "█" * 3
            s_10 = "     " + "█" * 3
            return [s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8, s_9, s_10]
        elif num == "8":
            s_1 = "█" * 8
            s_2 = "█" * 8
            s_3 = "█" * 3 + "  " + "█" * 3
            s_4 = "█" * 3 + "  " + "█" * 3
            s_5 = "█" * 8
            s_6 = "█" * 8
            s_7 = "█" * 3 + "  " + "█" * 3
            s_8 = "█" * 3 + "  " + "█" * 3
            s_9 = "█" * 8
            s_10 = "█" * 8
            return [s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8, s_9, s_10]
        elif num == "9":
            s_1 = "█" * 8
            s_2 = "█" * 8
            s_3 = "█" * 3 + "  " + "█" * 3
            s_4 = "█" * 3 + "  " + "█" * 3
            s_5 = "█" * 8
            s_6 = "█" * 8
            s_7 = "     " + "█" * 3
            s_8 = "     " + "█" * 3
            s_9 = "     " + "█" * 3
            s_10 = "     " + "█" * 3
            return [s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8, s_9, s_10]
        else:
            pass
    def draw_delimiter(self):
        s_1 = "           "
        s_2 = "           "
        s_3 = "    " + "█" * 3 + "    "
        s_4 = "    " + "█" * 3 + "    "
        s_5 = "           "
        s_6 = "           "
        s_7 = "    " + "█" * 3 + "    "
        s_8 = "    " + "█" * 3 + "    "
        s_9 = "           "
        s_10 = "           "
        return [s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8, s_9, s_10]
    def make_list(self):   
        tp = self.time_parts
        lst = [self.draw_number(tp[0]), self.draw_number(tp[1]),
                self.draw_delimiter(), self.draw_number(tp[3]), 
                self.draw_number(tp[4]), self.draw_delimiter(),
                self.draw_number(tp[6]), self.draw_number(tp[7])]
        transposed_lst = list(zip(*lst))
        return transposed_lst
    def draw_time(self):
        lst = self.make_list()
        str_1 = ""
        for i in lst:
            a = "   ".join(i) + "\n"
            str_1 = str_1 + a
        # flush=True - очищает буфер
        print(str_1, end = "", flush=True)
        # приостанавливает выполнение программы на 
        # количество секунд, указанных в скобках 
        time.sleep(0.15)
        # вычищает полностью экран
        os.system('cls')
def main():
    while True:
        tz_minsk = pytz.timezone("Europe/Minsk")
        ct_native = datetime.datetime.now()
        ct_minsk = (tz_minsk.localize(ct_native)).time()
        ct_str = ct_minsk.strftime("%H.%M.%S")
        ct_list = list(ct_str)
        time_now = Happy_time(ct_list)
        time_now.draw_time()
main()





