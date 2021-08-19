array_a=[[2,3,20],[4,20,1, 20],[2,3,4, [2, 10, 20]],8, 7, 20]

def forlist(array):
    for i in array:
        if type(i)==list:
            forlist(i)
        elif 20 in array:
            array.remove(20)
forlist(array_a)
print(array_a)

