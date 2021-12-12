file = open('test.txt')
# print(file.read())  # read all the contents of the file

# print(file.readline())  # read line by line
# print(file.readline())  # read line by line

# iterating by while loop
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()


# iterating by for loop
for line in file.readlines():
    print(line)

file.close()
