def binary_search(list,target):
    first = 0
    last = len(list)-1

    while first <= last:
        midpoint = (first + last )//2

        #A series of constant time operations
        if list[midpoint]==target:
            return midpoint
        elif list[midpoint]<target:
            first=midpoint + 1
        else:
            last=midpoint - 1

    return None

def binary_search(list,target):
    #returns the index position of the target found else returns None
    for i in range(0,len(list)):
        if list[i] ==target:
            return i

    return None

def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result=binary_search(numbers,12)
verify(result)

result=binary_search(numbers,6)
verify(result)