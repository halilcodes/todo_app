import glob

myfiles = glob.glob("*.py")
allfiles = glob.glob("*")

print(myfiles)
print(allfiles)

f_files = glob.glob("files/*.txt")

for filepath in f_files:
    print(filepath)
    with open(filepath, "r") as file:
        print(file.read())