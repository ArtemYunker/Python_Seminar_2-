# 3.	Задайте список из n чисел последовательности    (1+ 1/n)**n  выведите на экран их сумму.

n= int(input('введите число  '))

array=list(range(1,n+1))
print(array)
sum =0
for i in array:
    i=round((1+ 1/i)**i,3)
    sum = i+sum
    print(i)
print(f'Сумма = {sum}')
