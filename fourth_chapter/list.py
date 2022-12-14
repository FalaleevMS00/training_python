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
#Функция to_list() принимает неограниченное количество параметров.
#Обработайте их так, чтобы на выходе получить список из этих элементов.

def to_list(*args):
    return list(args)

#Николай задумался о поиске «бесполезного» числа на основании
# списка.
#Суть оного в следующем: он берет произвольный список чисел,
# находит самое большое из них, а затем делит его на длину списка.
#Студент пока не придумал, где может пригодиться подобное значение,
# но ищет у вас помощи в реализации такой функции useless(s).

def useless(s):
    max_value = max(s)
    len_list = len(s)
    return max_value / len_list

#Требуется создать функцию list_sort(lst),
# которая сортирует список чисел по убыванию их абсолютного значения.

def list_sort(lst):
    lst.sort(key=lambda x: abs(x), reverse=True)
    return lst

#На входе имеем список строк разной длины.
#Необходимо написать функцию all_eq(lst), которая вернет новый список из строк одинаковой длины.
#Длину итоговой строки определяем исходя из самой большой из них.
#Если конкретная строка короче самой длинной, дополнить ее нижними подчеркиваниями с правого края до требуемого количества символов.
#Расположение элементов начального списка не менять.

def all_eq(lst):
    max_str = max(lst, key=lambda x: len(x))
    len_max_str = len(max_str)
    new_lst = []
    for i in lst:
        count_need = len_max_str - len(i)
        new_i = i + count_need * "_"
        new_lst.append(new_i)
    return new_lst

