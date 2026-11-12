names = []
name = input("Name: ")
while name != "quit":
    names.append(name.title())
    name = input("Name: ")
print(names)
print(len(names))
print(f"First: {names[0]}")