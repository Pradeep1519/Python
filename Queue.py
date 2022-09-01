# in the Queue operation Queue is work on FFO(FIRST IN FIRST OUT)
# push (inseart)
# pop (delete)
# front (first element)
# rear (last element)
# display (display full stack)
l = []
while True:
    n = int(input('''enter the number
    1 push element
    2 pop element
    3 front element
    4 rear element
    5 dispaly queue
    6 exit'''))

    if n == 1:
        a = input("enter the element ")
        l.append(a)
        print(l)
    elif n == 2:
        if len(l) == 0:
            print("empty queue")
        else:
            del l[0]
            print(l)
    elif n == 3:
        if len(l) == 0:
            print("empty queue")
        else:
            print("first element in the queue", l[0])
    elif n == 4:
        if len(l) == 0:
            print("empty queue")
        else:
            print("last element in the queue", l[-1])
    elif n == 5:
        if len(l) == 0:
            print("empty queue")
        else:
            print("display queue", l)
    elif n == 6:
        break
    else:
        print("invalide operation")
