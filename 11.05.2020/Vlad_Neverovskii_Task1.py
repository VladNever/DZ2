# Первый способ через for:
def generator():
    counter = 0
    while True:
        if counter % 3 == 0:
            counter += 1
            yield "Василий"
        else:
            yield counter
            counter += 1    
def main ():
    for i in generator():
        inp = input("Введите что-нибудь: ")
        if inp == "q":
            break
        print(i)
main()

# Второй способ через While:
#def generator():
#    counter = 0
#    while True:
#        if counter % 3 == 0:
#            counter += 1
#            yield "Василий"
#        else:
#            yield counter
#            counter += 1
#def main():
#    # активация генератора. Почему нельзя сразу передать функцию генератора, 
#    # а только через переменную?  
#    a = generator()
#    while True:
#        inp = input("Введите что-нибудь: ")
#        if inp == "q":
#            break
#        b = next(a)
#        print(b)
#main() 