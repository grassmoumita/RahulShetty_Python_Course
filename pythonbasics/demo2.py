values=[1,2,"Moumita",4,5]     #List can hold different values and different data types also
print(values[0])
print(values[-1])      #-1 gives the last index values
print(values[1:4])
values.insert(3, "Demo")     # inserting values on 3rd index
print(values)
values.append("End")       #append will add always at the end of list
print(values)
values[2] = "MOUMITA"      #updating index value
print(values)
del values[0]      #deleting the 0th index value
print(values)

#Tuples
val = (1,2,"Mou",4,5)  # cannot modify or update tupple
print(val[1])


#Dictionary
dic = {"a":2, 4:"abc", "c":"Hello World"}
print(dic[4])
print(dic["c"])
print(dic)

#adding value in dictionary
dict = {}
dict["firstname"] = "Rahul"
dict["lastname"] = "Shetty"
print(dict)

dict["Gender"] = "Male"
print(dict)