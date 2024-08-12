print('Добро пожаловать в программу "Анализ оценок студентов"!')

print('1. Добавить оценку')
print('2. Показать все оценки')
print('3. Средняя оценка')
print('4. Наибольшая и наименьшая оценка')
print('5. Удалить оценку')
print('6. Выход')

list1 = []

while True:
    choise = int(input('Выберите действие:'))

    if choise == 1:
        item = int(input('Введите оценку :'))
        list1.append(item)

    if choise == 2:
        print('Список оценок :')    
        #print(','.join(list1))
        for item in list1:
             print(item)

    if choise == 3:  
   
     average = sum(list1) / len(list1)
     print(average)

    if choise == 4:
      
      #smallest_number = min(list1)
      #print("The smallest number is:", smallest_number)

      #largest_number = max(list1)
    # print("The largest number is:", largest_number)

      print(max(list1))

      print(min(list1))

    if choise == 5:
        item = int(input("Напишите, какой товар вы хотите удалить из списка: "))

        if item in list1:
            list1.remove(item)
            print("Оценка успешно удалёна")
       # else:
           # print("Указанной оценки нет в списке")

    if choise == 6:
              break
