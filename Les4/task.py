inp = input()
sum = 0

while inp != "stop":
    sum += int(inp)
    inp = input()

if (sum >= 0):
    print("Your profile is " + str(sum) + " euro")
else: 
    print("Your loss is " + str(-sum) + " euro")

