import os
import shutil

files = os.listdir("C:/python")

os.makedirs("C:/python/code", exist_ok = True)
os.makedirs("C:/python/text", exist_ok = True)
os.makedirs("C:/python/other", exist_ok = True)

for file in files:
    ext = os.path.splitext(file)[1]
    if os.path.isdir("C:/python/" + file):
        continue
    elif file == "task_mngr.py":
        continue
    elif ext == ".py":
        shutil.move("C:/python/" + file, "C:/python/code")
    elif ext == ".txt":
        shutil.move("C:/python/" + file, "C:/python/text")
    else:
        shutil.move("C:/python/" + file, "C:/python/other")

