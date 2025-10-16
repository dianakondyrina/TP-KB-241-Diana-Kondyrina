colors = ["blue", "red", "white", "pink", "yellow"]
print(colors)

def find_position(sort, value):
    for i in range(len(sort)):
        if value < sort[i]:
            return i
    return len(sort)

new_color = input("Введіть новий колір: ")

pos = find_position(colors, new_color)

print(f"Позиція для вставки: {pos}")

colors.insert(pos, new_color)

print("Список після вставки:", colors)