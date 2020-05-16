# one = 1
#just like anywhere else
# two = 2
# three = 3
one, two, three = 1, 2, 3

PI = 3.14

#global variable

print(one)
print(two)
print(three)
two = 4
print(two)
five = 3 + 2
print(five)

Decimal = 1.1
print(Decimal)

StringVar = "Hello" + "1"
print(StringVar)

def ExampleFunc():
    global PI
    newVar = "Test1"
    print(newVar)
    print(PI)
    return
ExampleFunc()
# print(newVar)

count = 0
print(count)
count = count + 1
print(count)
count += 1
print(count)
count *= 3
print(count)
count /= 2
print(count)








