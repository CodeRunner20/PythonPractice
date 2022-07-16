def appendtext(fname):
    with open(fname, 'a+') as f:
        f.write('Welcome to Python Programming. ')
        f.close()


file = open('file2.txt.txt')
print("File before append")
print(file.read())
appendtext('file2.txt.txt')
file1 = open('file2.txt.txt')
print("File after append")
print(file1.read())
file.close