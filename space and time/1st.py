def fun1(n):
    print(n * (n + 1) / 2)

def fun2(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(sum)

def fun3(n):
    sum = 0
    for i in range(1, n + 1):
        for j in range(i, i + 1):
            sum += 1
    print(sum)

fun1(4)
fun2(4)
fun3(4)