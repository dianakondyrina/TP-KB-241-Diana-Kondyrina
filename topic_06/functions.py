def log(message):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")


def addition(x, y):
    result = x + y
    log(f"Додавання: {x} + {y} = {result}")
    return result


def subtraction(x, y):
    result = x - y
    log(f"Віднімання: {x} - {y} = {result}")
    return result


def multiplication(x, y):
    result = x * y
    log(f"Множення: {x} * {y} = {result}")
    return result


def division(x, y):
    if y == 0:
        log(f"Помилка ділення: {x} / {y} — ділення на нуль")
        return "Помилка! Ділити на нуль не можна."
    result = x / y
    log(f"Ділення: {x} / {y} = {result}")
    return result

