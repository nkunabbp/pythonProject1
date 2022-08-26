def bubble_sort(ls):
    for i in range(len(ls) - 1):
        for j in range(len(ls) - 1):
            if ls[j] > ls[j + 1]:
                tmp = ls[j + 1]
                ls[j + 1] = ls[j]
                ls[j] = tmp
    return ls


def bubble_sort1(ls):
    for i in range(len(ls) - 1):
        for j in range(len(ls) - 1):
            if ls[j] < ls[j + 1]:
                tmp = ls[j + 1]
                ls[j + 1] = ls[j]
                ls[j] = tmp
    return ls


def myfind(ls, n):
    for i in range(len(ls)):
        if ls[i] == n:
            return i
    return -1


list1 = [1, 3, 5, 9, 13, 15]
list2 = [2, 4, 8, 10, 12, 18]
list3 = [7, 11, 17, 19]
list4 = [6, 14, 16, 20]
list5 = list1 + list2 + list3 + list4
print("Список всех листов:", list5)

opt = int(input("Для сортировки по возрастанию-1\nДля сортировки по убыванию - 2\nДля поиска-3\nВаш выбор:"))
if opt == 1:
    print(bubble_sort(list5))
elif opt == 2:
    print(bubble_sort1(list5))
elif opt == 3:
    n = int(input("Введите символ для поиска:"))
    a = myfind(list5, n)
    print("Ваши символ находится под индексом:", a)