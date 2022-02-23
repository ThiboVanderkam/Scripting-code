firstname = input("Give me your firstname: ")
familyname = input("Give me your lastname: ")
age = int(input("Give me your age: "))

# print(type(age))

print(firstname + familyname + str(age) + "years old")

if age >= 18:
    print("You are an adult")
elif age < 16:
    print("F U FAGGOT!")
else:
    print("Fokking baby")

print("end program")

for i in range(0, 10):
    print(i)

commando = input("Give me a commando, say stop to stop")

while commando != "stop":
    commando = input("Give me a commando, say stop to stop")