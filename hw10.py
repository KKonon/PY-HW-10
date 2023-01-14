# Даны вещественные положительные числа А,В,С. Необходимо выяснить, существуют ли треугольник со
# сторонам А В С.

sideA = int(input("Введите положительное число A: "))
sideB = int(input("Введите положительное число B: "))
sideC = int(input("Введите положительное число C: "))

if sideA < sideB + sideC or sideB < sideC + sideA or sideC < sideA + sideB:
    print("Треугольник АВС, существует!")
else:
    print("Треугольник АВС, не сущетсвует")

# Задание 2 | Дано целое число n (n находится в диапазоне от 1 до 99), определяющее возраст человека в годах.
# Для этого числа необходимо напечатать фразу "мне n лет".
# Учитывайте, что при некоторых значениях n слово "лет" нужно заменить на слово "год" или "года".

userAge = int(input("Введите ваш возвраст: "))

if userAge == 1 or userAge == 21 or userAge == 31 or userAge == 41 or userAge == 51 or userAge == 61 or userAge == 71 or userAge == 81 or userAge == 91:
    print("Ваш возвраст: ", userAge, "год")
elif userAge > 1 and userAge <= 4 or userAge > 21 and userAge <= 24 or userAge > 31 and userAge <= 34 or userAge > 41 and userAge <= 44 or userAge > 51 and userAge <= 54 or userAge > 61 and userAge <= 64 or userAge > 71 and userAge <= 74 or userAge > 81 and userAge <= 84 or userAge > 91 and userAge <= 94:
    print("Ваш возвраст: ", userAge, "года")
elif userAge > 4 and userAge <= 20 or userAge > 24 and userAge <= 30 or userAge > 34 and userAge <= 40 or userAge > 44 and userAge <= 50 or userAge > 54 and userAge <= 60 or userAge > 64 and userAge <= 70 or userAge > 74 and userAge <= 80 or userAge > 84 and userAge <= 90 or userAge > 94 and userAge <= 99:
    print("Ваш возвраст: ", userAge, "лет")
else:
    print("Введите возвраст от 1 до 99 лет")
