party={
    "date":"31.10.27",
    "name":"Halloween",
    "dress_code":"costumes"
}

print(party)

party.update({"Where":"Vegas"})
print(party)

del party["date"]
print (party)

party.clear()
print(party)

party={
    "date":"31.10.27",
    "name":"Halloween",
    "dress_code":"costumes"
}

print(party.keys())

print(party.values())

print(party.items()
      )