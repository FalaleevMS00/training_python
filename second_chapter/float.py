#Напишите функцию to_float(num), которая преобразует любое число в число с плавающей точкой.
#Если в качестве аргумента передан другой тип данных, она возвращает «Невозможно преобразовать».
def to_float(num):
    if isinstance(num, (int, float)):
        return float(num)
    return "Невозможно преобразовать"

print(to_float(3))