import os
# file = open("Test.py")
# for x in file:
#     print(x+"==")
# file.close()

File2 = open("Demo.txt", "w")

File2.write("This is the 'w' method which writes over the content of the file")
File2.close()
file2 = open("Demo.txt", "r")
print(file2.read())

file2.close()
File2 = open("Demo.txt", "a")

File2.write("  This is the appended part")

File2.close()

file2 = open("Demo.txt", "r")

print(file2.read())


if os.path.exists("a;fajk.txt"):
    os.remove("a;fajk.txt")
else:
    print("File doesn't exist")


