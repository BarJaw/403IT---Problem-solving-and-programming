# Function which prints all of the numbers from n to 0
def countdown(n):
    print(n)
    if n == 0:
        return 0
    return countdown(n - 1)

# Function which returns factorial of a given number
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Function which returns the nth number of the Fibonacci sequence
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
