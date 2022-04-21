phonebook = {}

phonebook["saad"] = 1724568773
phonebook["link3"] = 9678123123
phonebook["GP Help"] = 123
phonebook["Sample number"] = 1982356762

print(phonebook)

for name, number in phonebook.items():
    if len(str(number)) == 10:
        print("{}'s number is 0{}".format(name, number))
    else:
        print("{}'s number is {}".format(name, number))

del phonebook["GP Help"] # can also be done by "phonebook.pop("GP Help")"

print("")

for name, number in phonebook.items():
    if len(str(number)) == 10:
        print("{}'s number is 0{}".format(name, number))
    else:
        print("{}'s number is {}".format(name, number))
