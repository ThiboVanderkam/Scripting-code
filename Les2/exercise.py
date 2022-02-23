kilos = float(input("HELLO PERSON? HOW MANY KG SAUSAGES DO YOU WANT? "))
price = kilos * 5.5
print("Here is", kilos, "kg for", price, "euros. Give me your Money!")
payment = float(input())

while payment < price:
    print("That is nog enough! Give me your money!")
    payment = float(input())

change = payment - price
print("Here you go", change, "euros back.")