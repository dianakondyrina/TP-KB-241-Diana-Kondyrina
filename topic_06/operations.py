from functions import addition, subtraction, multiplication, division

def enter_num(prompt):
    while True:
        num_input = input(prompt)

        if num_input.lower() == "exit":
            return None
        try:
            number = float(num_input)
            return number
        except ValueError:
            print("Помилка: введіть число!")


def enter_oper():
    while True:
        operator = input('Виберіть операцію (+, -, *, /): ')
        if operator not in ['+', '-', '*', '/']:
            print('Неправильна операція')
            continue
        return operator

def operation(num1, num2, operator):
    if operator == '+':
        return addition(num1, num2)
    elif operator == '-':
        return subtraction(num1, num2)
    elif operator == '*':
        return multiplication(num1, num2)
    elif operator == '/':
        return division(num1, num2)

