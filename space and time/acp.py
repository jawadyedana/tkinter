def multiply_iterative(n, m):
    result = 0
    for _ in range(m):
        result += n
    return result

def multiply_recursive(n, m):
    if m == 0:
        return 0
    elif m < 0:
        return -multiply_recursive(n, -m)
    else:
        return n + multiply_recursive(n, m - 1)

def main():
    n = int(input("Enter the first number (N): "))
    m = int(input("Enter the second number (M): "))

    iterative_result = multiply_iterative(n, m)
    recursive_result = multiply_recursive(n, m)

    print(f"Iterative multiplication: {n} * {m} = {iterative_result}")
    print(f"Recursive multiplication: {n} * {m} = {recursive_result}")
