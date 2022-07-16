import os
path = os.getcwd()
print(os.getcwd())
dir_list = os.listdir()
print("Files inside the current working directory: ")
for a in dir_list:
    if os.path.isfile(a):
        print(a)