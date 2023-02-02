new_list=[1,2,3]    #stored elsewhere and the array stores references
result=new_list[0]  #assigning an arra toanoter varable


#searching for an element
if 1 in new_list:print(True)

#comparison operation
for n in new_list:
    if n is 1:
        print(True)

#Inserting operations
#inserting using an index value - linear runtime operation
#appending - constant time operation - has an ammortized constant space complexity
#extend - O(k) - k = number of elements added to the list
#Delete - 

#liked list
#A linear data structure where each element in the list is contained in a separate object called a Node
#a node models two pieces of information an ndividual item of the data we want to store and a reference to the next node in the list
# The first node in the linked list is the head of the list while the last node is called the Tail
#The only reference kept is the head
#nodes - self referential objects - each node stores a reference to the node before and after it
