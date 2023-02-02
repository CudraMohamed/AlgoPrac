class Node:
    # an object for storing a single node of a linked list
    #Models two attrobutes - data ad the link to the next node in the list

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

class LinkedList:
    heas = None

    #singly linked list
    def __init__(self):
        self.head =None

    def is_empty(self):
        return self.head ==None

    def size(self):
        current = self.head
        count = 0
        
        while current:
            count += 1
            current = current.next_node
        return count

    def add(self,data):
        #add new node
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        #search for the first code containing data that matches the key
        #return the node od none if not found
        #takes 0(n) time

        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def __repr__(self):
        #return a tring representation of the list
        #take 0(n) time

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("Head: %s" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '-> '.join(nodes)