import os
print("current directory:",os.getcwd())
print("files in current directory:",os.listdir())
os.mkdir("test_folder")
print("created folder:test_folder")
os.rmdir("test_folder")
print("removed folder:test_folder")