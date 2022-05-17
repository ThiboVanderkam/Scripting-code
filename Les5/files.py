from pathlib import Path
import os

# print(type(os.getcwd()))
# print(type(Path.cwd()))

pythonFolderPath = Path(r"C:\Users\thibo\OneDrive\Bureaublad\python_map\python.txt")

# print("Bestaat de folder/file?", pythonFolderPath.exists())
# print("Is het een folder?", pythonFolderPath.is_dir())
# print("Is het een file?", pythonFolderPath.is_file())
# print("Is het een parent folder?", pythonFolderPath.parent)
# print("Welke extension?", pythonFolderPath.suffix)
# print("Welke bestandsnaam?", pythonFolderPath.stem)
# print("Full file name?", pythonFolderPath.name)

# file = Path(__file__)
# print(file.name)

# writing
# file = open("log.txt", "a")
# file.write("Collin was hier om 11:40")
# file.close()

#reading
file = open("log.txt", "r")
fullText = file.read()
print(fullText)
file.close()

