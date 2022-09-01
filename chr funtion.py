# in the chr() function it will takes in an intiger value and convert into string and charecter value
y=chr(65)  # chr function
print(type(y),y) # print the type and value

y=chr(66)
print(type(y),y)

y=chr(67)
print(type(y),y)

a=int(input("enter the value above the 64"))
for i in range(65,a+1):
    print(chr(i))