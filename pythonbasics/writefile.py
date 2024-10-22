#read the file and store all the lines in a list
#reverse the list
#write the list back to the file

with open('text.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('text.txt', 'w') as writer:
        for i in reversed(content):
            writer.write(i)

