from operations import enter_num, enter_oper, operation
from functions import log

print("Напишіть числа чи 'exit' аби закінчити")
log("Запуск калькулятора")

while True:
    num1 = enter_num("Введіть перше число: ")
    if num1 is None:
        break

    num2 = enter_num("Введіть друге число: ")
    if num2 is None:
        break

    operator = enter_oper()
    result = operation(num1, num2, operator)

    print("Результат:", result)
    log(f"Виведено результат: {result}")

log("Завершення роботи\n")
