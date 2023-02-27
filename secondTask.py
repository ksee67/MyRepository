print("Подсчёт дней")  #Выводим сообщение
i =1
while i == 1:
    findTheYear  = input("Подсчёт дней \nВыберите год который хотите подсчитать:\n"  
              "1 - Високосный (366 дней) \n" 
              "2 - Невисокосный (365 дней) \n"
              "3 - Выйти \n")
    if findTheYear == '1': 
        january = [3, 1]        
        february = [2, 9]
        march = [3, 1]
        april = [3, 0]
        may = [3, 1]
        june = [3, 0]
        july = [3, 1]
        august = [3, 1]
        september = [3, 0]
        october = [3, 1]
        november = [3, 0]
        december = [3, 1]
        reply = sum(january) + sum(february) + sum(march) + sum(april) +sum(may) + sum(june) + sum(july) + sum(august) + sum(september) +sum(october) + sum(november) + sum(december) 
        print(f"Високосный год: {reply} ☘")
    elif findTheYear == '2': 
        january = [3, 1]        
        february = [2, 8]
        march = [3, 1]
        april = [3, 0]
        may = [3, 1]
        june = [3, 0]
        july = [3, 1]
        august = [3, 1]
        september = [3, 0]
        october = [3, 1]
        november = [3, 0]
        december = [3, 1]
        reply = sum(january) + sum(february) + sum(march) + sum(april) +sum(may) + sum(june) + sum(july) + sum(august) + sum(september) +sum(october) + sum(november) + sum(december) 
        print(f"Невисокосный год: {reply} ☘")
    elif findTheYear == '3':
        exit() 
    else: 
        print("Выбрана неверная операция!") 
