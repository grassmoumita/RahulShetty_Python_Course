str = "Google.com"
str1 = "Academy"
str2 = "Google"


print(str[1])     #print the 2nd index character of the string
print(str[0:5])    #substring, from 0th index to 4th index

print(str+str1)    #concatenate 2 string

print(str2 in str)     #to check if a string is present in another string

var = str.split(".")        #split a string
print(var)        #['Google', 'com']
print(var[0])

str4 = "    great    "
print(str4.strip())      #strip is used to remove space on both end
print(str4.lstrip())       #lstrip is used to remove space on left end only
print(str4.rstrip())       #rstrip is used to remove space on right end only