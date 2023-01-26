print("Калькулятор")  #Выводим сообщение
count= float(input("Введите кол-во операций: "))
num1 = float(input("Введите первое число: ")) 

i =1
while i <= count:
    action = input("Калькулятор \nВыберите цифру действия которое хотите сделать:\n"  
              "1 - Сложение \n" 
              "2 - Вычетание \n"
              "3 - Умножение \n"
              "4 - Деление \n"
              "5 - Процент от числа \n"
              "6 - Выйти \n")
    if action == '1': 
         num2 = float(input("Введите второе число: ")) 
         num1 = num1 + num2
         i+=1
         print("Число: " + str(num1)) 
    elif action == '2': 
        num2 = float(input("Введите второе число: ")) 
        num1 = num1 - num2
        i+=1
        print("Число: " + str(num1))
    elif action == '3':
        num2 = float(input("Введите второе число: ")) 
        num1 = num1 * num2
        i+=1
        print("Число: " + str(num1))
    elif action == '4':
        num2 = float(input("Введите второе число: ")) 
        if (num2 == 0): # Проверка на ноль
            print("Число: " + str(num1))
            print("Делить на ноль нельзя!")
            i-=1
        else: 
            num1 = num1 / num2
            i+=1
            print(num1)
        print("Число: " + str(num1))
    elif action == '5':
        num2 = float(input("Введите второе число: ")) 
        num1 = num1 % num2
        i+=1
        print("Число: " + str(num1))
    elif action == '6':
        exit() 
    else: 
        print("Выбрана неверная операция!") 
        i-=1



