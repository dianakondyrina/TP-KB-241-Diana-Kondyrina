
def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y


while True:
    a = input("Напишіть перше число або 'exit' для виходу: ")
    if a.lower() == "exit":
        break

    b = input("Напишіть друге число: ")
    if b.lower() == "exit":
        break


    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print("Помилка, введіть число")
        continue

    operation = input("Оберіть операцію: ")
    if operation.lower() == "exit":
        print("Програму завершено")
        break

    match operation:
        case "+":
            print(f"Результат: {addition(a, b)}")
        case "-":
            print(f"Результат: {subtraction(a, b)}")
        case "*":
            print(f"Результат: {multiplication(a, b)}")
        case "/":
            try:
                print(f"Результат: {division(a, b)}")
            except ZeroDivisionError:
                print("На 0 не ділять")