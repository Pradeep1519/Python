# comrehension means we are enter the multiple elements in the list in sort time
l = [m for m in range(1, 101)]  # m is a list element and we applied for loop and in the for loop we are taking the
# variable m becouse in the comrehension both side taking same value and finally enter the range to run the loop
print(l)  # print the
print()
# conditional comprehension
p = [n for n in range(1, 101) if
     n % 2 == 0]  # in the provide the condion is the comprehension print only even numbers in
# the list between 1 to 100
print(p)  # print the even numbers in the list between 1 to 100
print()
# convert string in to list in shepret form
r = 'heelo pradeed kumar '  # string
d = [g for g in r]  # we are not applied range in the for loop becouse range provide only for numbers
print(d)  # print the string in the list
