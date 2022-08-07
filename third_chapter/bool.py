#Напишите функцию dislike_6(a), которая всегда возвращает True, если только
# не передается число 6 типа int или типа float (в данном случае она вернет «Только не 6!»).

def dislike_6(a):
    if isinstance(a, (int, float)) and int(a) == 6:
        return "Только не 6!"
    return True
