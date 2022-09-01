# in the stack operation stack is work on LIFO(LAST IN FIRST OUT)
# push (inseart)
# pop (delete)
# peek (print last element)
# display (display full stack)
l = []
while True:
    n = int(input(''' enter the value
    1 push element
    2 pop element
    3 peek element
    4 display element
    5 exit'''))
    if n == 1:
        p = input("enetr the element")
        s = l.append(p)
        print(l)
        print(s)
    elif n == 2:
        if len(l) == 0:
            print("empty stack")
        else:
            o = l.pop()
            print(o)
            print(l)
    elif n == 3:
        print("this is the last stack vale", l[-1])
    elif n == 4:
        print("stack", l)
    elif n == 5:
        break
