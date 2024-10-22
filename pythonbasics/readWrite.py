file = open('text.txt')
#read all the content
#print(file.read())       #read the full content
#print(file.read(2))    # read only first 2 character

#read line by line
# print(file.readline())      #1st line will read
# print(file.readline())      #2nd line will read


#read all line at a time by readline method
# line = file.readline()
# while line!= "":
#     print(line)
#     line=file.readline()

#readlines() method
# print(file.readlines())     #readlines() methis will store all the line values in a list ['afv\n', 'bfgf\n', 'cfbgf\n', 'dfg\n', 'efffff']
line = file.readlines()
for i in line:         #using for loop we can exact all the values and read line by line
    print(i)

file.close()
