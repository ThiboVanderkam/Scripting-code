from pathlib import Path
import os, shutil, zipfile

if not Path("logs").exists():
    print("Folder bestaat niet")
    os.mkdir("logs")

#shutil.copy("log.txt", "logs/copy_log.txt")
#shutil.move("log.txt", "logs/log.txt")
#shutil.rmtree("logs")

#newzip = zipfile.ZipFile("logs.zip", "w")
#newzip.write("logs/log.txt")
#newzip.extractall()
#newzip.close()