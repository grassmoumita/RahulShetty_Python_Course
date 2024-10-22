itemscart = 0

if itemscart != 2:
    pass
    #raise Exception("Product cart is not matching")

assert (itemscart==0)

#try catch

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except:
    print("somehow i reached the block because there is a failure in try block")


try:
    with open('text.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print("cleaning up resources")