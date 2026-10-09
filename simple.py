print("Введите число от 1 до 25, чтобы проверить простое ли оно")
n=int(input())
if 1 <= n <= 25:
    a=0
    for i in range(2, n):
        if n % i == 0:
            a= a + 1
    if n >= 2 and a==0:
            print("Y")    
    else:
            print("N")  
else:
        print("Число находится вне заданного промежутка")            