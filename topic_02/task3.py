
a = float(input("Напишіть перше число: "))
b = float(input("Напишіть друге число: "))
operation = input("Оберіть операцію: ")

match operation:
   case "+":
      print(f"Результат: {a + b}")
   case "-":
      print(f"Результат: {a - b}")
   case "*":
      print(f"Результат: {a * b}")
   case "/":
      if b == 0:
       print("на 0 не ділять")
      else:
          print(f"Результат: {a / b}")