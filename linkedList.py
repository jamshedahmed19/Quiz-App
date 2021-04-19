class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  
 
class LinkedList:
    def __init__(self):
        self.head = None
 
 
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def selectionSort(self): 
  
        a = b = self.head 

        # While b is not the last node 
        while b.next: 

            c = d = b.next

            # While d is pointing to a valid node 
            while d: 

                if b.data < d.data: 

                    # If d appears immediately after b 
                    if b.next == d: 

                        # Case 1: b is the head 
                        # of the linked list 
                        if b == self.head: 

                            # Move d before b 
                            b.next = d.next
                            d.next = b 

                            # Swap b and d pointers 
                            b, d = d, b 
                            c = d 

                            # Update the head 
                            self.head = b 

                            # Skip to the next element 
                            # as it is already in order 
                            d = d.next

                        # Case 2: b is not the head 
                        # of the linked list 
                        else: 

                            # Move d before b 
                            b.next = d.next
                            d.next = b 
                            a.next = d 

                            # Swap b and d pointers 
                            b, d = d, b 
                            c = d 

                            # Skip to the next element 
                            # as it is already in order 
                            d = d.next

                    # If b and d have some non-zero 
                    # number of nodes in between them 
                    else:

                        # Case 3: b is the head 
                        # of the linked list 
                        if b == self.head: 

                            # Swap b.next and d.next 
                            r = b.next
                            b.next = d.next
                            d.next = r 
                            c.next = b 

                            # Swap b and d pointers 
                            b, d = d, b 
                            c = d 

                            # Skip to the next element 
                            # as it is already in order 
                            d = d.next

                            # Update the head 
                            self.head = b 

                        # Case 4: b is not the head
                        # of the linked list 
                        else: 

                            # Swap b.next and d.next 
                            r = b.next
                            b.next = d.next
                            d.next = r 
                            c.next = b 
                            a.next = d 

                            # Swap b and d pointers 
                            b, d = d, b 
                            c = d 

                            # Skip to the next element 
                            # as it is already in order 
                            d = d.next

                else:

                    # Update c and skip to the next element 
                    # as it is already in order 
                    c = d 
                    d = d.next

            a = b 
            b = b.next

        return self.head 
    
    def returnNthfromfirst(self, index):
        current = self.head  # Initialise temp
        count = 0  # Index of current node
 
        # Loop while end of linked list is not reached
        while (current):
            if (count == index):
                return current.data
            count += 1
            current = current.next
 
        # if we get to this line, the caller was asking
        # for a non-existent element so we assert fail
        return 0
    
    def getCount(self):
        temp = self.head # Initialise temp
        count = 0 # Initialise count
  
        # Loop while end of linked list is not reached
        while (temp):
            count += 1
            temp = temp.next
        return count    