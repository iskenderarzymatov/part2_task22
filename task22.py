
gg = input("Введите температуру и укажите F или C: ")
gradus = gg.upper()
print(gradus)
list_gradus = (list(gradus))
str_gradus = ""
list_num_gradus = []

for i in list_gradus:                   # Выбираем только цифры из списка list_gradus
    try:
        list_num_gradus.append(int(i))       # и помещаем их в список num_gradus
    except ValueError:             # если выйдит ощибка(букву нельзя преобразовать в int)то продолжить цикл
        continue

for i in list_num_gradus:                # превращаем список из цифр в одну строку с помощью конкатенации
    str_gradus += str(i)            # чтобы цифры на суммировались

if str_gradus == "":
    print("Не правильный ввод.")
    print("Введите примерно так: 35C или 35F")
else:
    num_gradus = int(str_gradus)

    if gradus.count("F") == 1 and gradus.count("C") == 0 and gradus[:-2].isnumeric(): # если строка сожержит только "F" и не содержит "C" и все элементы кроме последнего цифры
        print("По Цельсию она равна:", round(5/9 * (num_gradus - 32), 2))
    elif gradus.count("C") == 1 and gradus.count("F") == 0 and gradus[:-2].isnumeric(): # а если строка сожержит только "C" и не содержит "F" и все элементы кроме последнего цифры
        print("По Фаренгейту она равна:", round(9/5 * num_gradus + 32, 2))
    else:
        print("Не правильный ввод.")
        print("Введите примерно так: 35C или 35F")
