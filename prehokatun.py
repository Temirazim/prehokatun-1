#Задача 1
# Есть список:
#Выведите все элементы, которые больше 5.
a = [1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for x in a:
    if x > 5:
        print(x) 
#Задача 2
#Есть набор чисел digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
#Поделить каждое число из digits на 9 и вывести на экран.
digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
for x in digits:
    print(x/9)
Задача 3
#fruits = ('banana','stawberry','apple','orange','limon','ananas')
# Выведите первый и последний элемент списка.
fruits = ('banana','stawberry','apple','orange','limon','ananas')
fruits = list(fruits)
print(fruits[0])
print(fruits[5])
# Задача 4 
# Здесь замешаны разные типы данных. 
# Если вы уверены что логика написана правильно, но оно всё равно не работает скорее всего вы справились с заданием
 
#spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
#spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
# Напишите программу, которая берёт массив данных spisok2 и выводит только те элементы из spisok_2, которых нет в spisok_1.
spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
a = set(spisok_1)
b = set(spisok_2)
c = set(b).difference(set(a))
# print(c)
# Задача 5
# Напишите программу, которая выводит чётные числа из списка длиною 300 объектов и останавливается, если встречает число 237.
a = [ i for i in range(1, 300)]
for x in a:
    if x == 237:
        break
    elif x %2 == 0:
        print(x)


a = list(i for i in range(0, 300))
i = 0
while i < 237 and i %2 == 0:
    i +=1
    print(i)