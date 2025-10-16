
while True:
    a = input("Напишіть перше число або 'exit' для виходу: ")
    if a.lower() == "exit":
        break

    b = input("Напишіть друге число: ")
    if b.lower() == "exit":
        break
    operation = input("Оберіть операцію: ")
    if operation.lower() == "exit":
        print("Програму завершено.")
        break

    a = float(a)
    b = float(b)

    match operation:
        case "+":
            print(f"Результат: {a + b}")
        case "-":
            print(f"Результат: {a - b}")
        case "*":
            print(f"Результат: {a * b}")
        case "/":
            if b == 0:
                print("На 0 не ділять")
            else:
                print(f"Результат: {a / b}")
        case _:
            print("Невідома операція!")