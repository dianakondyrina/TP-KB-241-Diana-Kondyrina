import lab_02

def test_load_csv():
    lab_02.students.clear()
    test_data = [
        {"name": "A", "phone": "1", "address": "a", "date": "1"},
        {"name": "B", "phone": "2", "address": "b", "date": "2"}
    ]

    lab_02.students.extend(test_data)

    assert len(lab_02.students) == 2
    assert lab_02.students[0]["name"] == "A"

def test_add_student():
    lab_02.students.clear()
    lab_02.students.append({"name": "Bob", "phone": "1", "address": "a", "date": "1"})
    lab_02.students.append({"name": "Zak", "phone": "2", "address": "b", "date": "2"})

    new_item = {"name": "Emma", "phone": "3", "address": "c", "date": "3"}

    pos = 0
    for s in lab_02.students:
        if new_item["name"] > s["name"]:
            pos += 1
        else:
            break

    lab_02.students.insert(pos, new_item)

    assert lab_02.students[1]["name"] == "Emma"
    assert lab_02.students[0]["name"] == "Bob"
    assert lab_02.students[2]["name"] == "Zak"

def test_delete_student():
    lab_02.students.clear()
    lab_02.students.append({"name": "Bob", "phone": "1", "address": "a", "date": "1"})

    for s in lab_02.students:
        if s["name"] == "Bob":
            lab_02.students.remove(s)
            break

    assert len(lab_02.students) == 0


def test_update_student():
    lab_02.students.clear()
    lab_02.students.append({"name": "Bob", "phone": "1", "address": "a", "date": "1"})

    for s in lab_02.students:
        if s["name"] == "Bob":
            lab_02.students.remove(s)
            break

    new_item = {"name": "Emma", "phone": "2", "address": "b", "date": "2"}

    pos = 0
    for s in lab_02.students:
        if new_item["name"] > s["name"]:
            pos += 1
        else:
            break

    lab_02.students.insert(pos, new_item)

    assert lab_02.students[0]["name"] == "Emma"

def test_save_csv():
    lab_02.students.clear()
    lab_02.students.append({"name": "Bob", "phone": "1", "address": "a", "date": "1"})

   
    lab_02.save_CSV()

    with open("lab2_out.csv", encoding="utf-8") as f:
        data = f.read()

    assert "name,phone,address,date" in data
    assert "Bob" in data
