firstname = input("Give me your firstname\n")
lastname = input("Give me your lastname\n")
age = int(input("Give me your age\n"))
fullname = firstname + " " + lastname

if age < 18:
    print("YOU CAN NOT ENTER, 2 YOUNG")
elif age > 65:
    print("YOU CAN NOT ENTER, 2 OLD")
else:
    print("You can enter")

print(fullname + " is " + str(age) + " jaar oud")