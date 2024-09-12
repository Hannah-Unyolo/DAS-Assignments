names = ("Hannah","Unyolo","Konemi","Pempho")
print(type(names))

# adding item in a tuple
secondnames = list(names)
secondnames.append("Keera")
names = tuple(secondnames)
print(names)


# adding a tuple to a tuple
name = ("Tina",)
names += name
print(names)


# removing items in a tuple
removenames = list(names)
removenames.remove("Pempho")
names = tuple(removenames)
print(names)

# deleting the whole tuple
del names
print(names)