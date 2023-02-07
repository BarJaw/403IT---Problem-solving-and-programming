def get_input():
    number = int(input("Input a number: "))
    return number

def validate_input(number):
    if number > 0:
        return True
    return False

def calculate_square(number):
    return number ** 2

def print_result(result):
    print(f"Square of your number is {result}")

def main():
    num = get_input()
    is_valid = validate_input(num)
    if is_valid:
        result = calculate_square(num)
        print_result(result)

main()