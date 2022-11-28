# 5.	Реализуйте алгоритм перемешивания списка
# (shuffle использовать нельзя, другие методы из библиотеки random - можно).

from random import randint

n = int(input('введите число  '))

array = list(range(-n, n + 1))
print(array)

array2 = array[:]
arra2_length = len(array)

for i in range(arra2_length):
    index = randint(0, arra2_length - 1)
    temp = array2[i]
    array2[i] = array2[index]
    array2[index] = temp

print(array2)
