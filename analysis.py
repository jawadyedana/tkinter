def counter(n):
 if n == 0:
    print("the end of the counter")
    return
 print("counter is at:", n)
 counter(n - 1)

counter(5)