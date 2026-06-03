import os

files = os.listdir("C:/python/test_rename")

for i, file in enumerate(files, 1):
    os.rename("C:/python/test_rename/" + file, "C:/python/test_rename/" + str(i) + "_" + file)