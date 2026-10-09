print("Введите число")
n = int(input())
x = 0
if 1 <= n <= 100000:
    while n >= 3:
        n -= 3
        x += 1
    while n > 0:
        n -= 1
        x += 1
        
    print(x)
else:
    print("Введите другое значение")