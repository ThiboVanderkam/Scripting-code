from tabnanny import check


def checkIfPositive(number):
    if (number >= 0):
        return True
    else:
        return False

print(checkIfPositive(-69))