x = int(input('Количество красных машин: '))
y = int(input('Количество белых машин: '))
result = ''
if (2 * y < x) or (2 * x < y):
    print('Нет решения')
elif x >= y:
    z = x - y
    for _ in range(z):
        result += 'RWR'
    for _ in range(y - z):
        result += 'RW'
else:
    z = y - x
    for _ in range(z):
        result += 'WRW'
    for _ in range(x - z):
        result += 'WR'
print(result)
