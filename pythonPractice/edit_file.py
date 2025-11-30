# Write to a File
# Write a program to create a text file and write some content to it.
# Using file functions like write and open.


def write_to_file():
    file = open("example.txt", "w")
    file.write("Hello, World!")
    file.close()

def read_file():
    file = open("example.txt", "r")
    print(file.read())
    file.close()    

write_to_file()
read_file()

