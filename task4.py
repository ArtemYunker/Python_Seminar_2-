# 4.	Задайте числами список из N элементов, заполненных из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

n = int(input('введите число  '))

array = list(range(-n, n + 1))
print(array)

path = 'file.txt'
data = open('file.txt', 'r')

for line in data:
    print(line)
string = line


res = [int(i) for i in string.split() if i.isdigit()]
print(res)
m = res[0]
k = res[1]

data.close()

result = array[m]*array[k]

print(result)
