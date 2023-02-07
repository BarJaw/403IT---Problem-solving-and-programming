def countdown(n):
    print(n)
    if n == 0:
        return 0
    return countdown(n - 1)

# countdown(10)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
    
print(factorial(5))

# 0 1 1 2 3 5 8
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))

