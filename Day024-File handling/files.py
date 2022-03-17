# basic way to open a files
file=open('my_file.txt')
contents=file.read()
print(contents)
file.close()        # we need to close file manually

# open file using 'with' keyword
# using this file is auto close after use
# with open("my_file.txt") as file:
#     contents=file.read()
#     print(contents)

with open('my_file.txt',mode='a') as file:
    file.write('new text\n')

