a = float(input("Напишіть перше число: "))
b = float(input("Напишіть друге число: "))
operation = input("Оберіть операцію: ")

if operation == "+":
     print(f"Результат: {a + b}")
elif operation == "-":
    print(f"Результат: {a - b}")
elif operation == "*":
    print(f"Результат: {a * b}")
else:
    if b == 0:
              print(f"на 0 не ділять")
             
    else:
                print(f"Результат: {a / b}")


