# we are use format function the format function is use to suppose that any name and any number
# you stor in the string and string is alredy created at the point the format funtion use with the help of place holder
# named indexes
p = "wellcome to {pname}{nname}".format(pname="my ", nname="home")  # this is the name indexing
print(p)
print() # space
# number indexing
r = "welcome to {0}{1}".format("my ", "home")  # tis is the number indexing
print(r)
print() # space
# empty indexing
a = "wellcome to {}{}".format("my ", "home")  # tis is the empty indexing
print(a)  # this is the print statement

print() # space
b = "wellcome to {a}{b}".format(a="my ", b="home") # we are making the variable
print(b)
print() # space
c = "wellcome to {d:10}{e}".format(d="my ", e="home") #{d:10} is the d is the variable and 10 is the space size
print(c)
print() # space
f = "wellcome to {g:^10}{h}".format(g="my ", h="home") # ^ this sign i use the vale print in the last and first  and
# i will print the middle in the space 10
print(f)