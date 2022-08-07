#Дан произвольный список.
#Представьте его в обратном порядке.
def remove(spisok):
    return spisok[::-1]

#Напишите функцию change(lst), которая принимает список
# и меняет местами его первый и последний элемент.
# В исходном списке минимум 2 элемента.
def change(lst):
    lst_first = lst[0]
    lst_last = lst[-1]
    lst[0] = lst_last
    lst[-1] = lst_first
    return lst
