greeting = "Good Morning"
a=4

if greeting == "Morning":
    print("condition matches")
else:
    print("condition not matched")

if a>2:
    print("condition matches")
else:
    print("condition not matched")
print("If else condition completed")

obj = [2,3,5,7,9]
for i in obj:
    print(i)
    print(i*2)

#sum of 5 natural numbers
sum=0
for i in range(1,6):
    print(i)
    sum=sum+i
print(sum)

for i in range(1,10,2):        # i will increment by 2
    print(i)

for i in range(10):     #start from 0 when do not give range 1st value
    print(i)
