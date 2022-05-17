from pathlib import Path
# C:\Users\thibo\Documents\IMS\Fase 1\Semester 2\Scripting\Scripting-code\Les5\log.txt
inp = input("Geef een pad (of een kikker)  ")
pythonPath = Path(inp)

if (pythonPath.exists and pythonPath.is_file()):
    inp = int(input("welke regel moet weg? "))
    file = open(pythonPath, "r")
    lines = file.readlines()
    file.close()
    del lines[inp - 1]
    file = open(pythonPath, "w")
    for item in lines:
        file.write(item)
    
    file.close()
    file = open(pythonPath, "r")
    fullText = file.read()
    file.close()
    print(fullText)
    print("lijn", inp,"is niet meer")
else:
    print("file bestaat niet")