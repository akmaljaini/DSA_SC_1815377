#group member
# Muhammad Akmal 1815377
# Khairul Izham 1816045
# Haliza Rahim 1826502
# Sarah Hanani 1912850



class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = None

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

class MyLList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def count(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node
    
    def addtail(self, item):
        new_node = Node(item)
        new_node.set_data(item)
        current = self.head
        while current.get_next() != None:
                current = current.get_next()
        current.set_next(new_node)

    def removehead(self): 
        if(self.head != None):
            temp = self.head
            self.head = self.head.next_node
            temp = None

    def removetail(self):
        temp = self.head
        while(temp.next_node is not None):
            prev  = temp
            temp = temp.next_node
        prev.next_node = None
    
    def delete(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current == None:
                print("The entered number does not exist within the list!")
                break

            if current.get_data() == item:
                found=True
            else:
                previous= current
                current=current.get_next()

        if found:
            if previous == None:
                self.head = current.next_node
                
            else:
                previous.set_next(current.next_node)
    
 
    def reverse(self): 
        previous = None
        current = self.head
        while current is not None:
            next = current.next_node
            current.next_node = previous
            previous = current
            current = next
        self.head = previous


            
    def printList(self):
        node = self.head
        while node != None:
            print("|",node.data,"|"," -->", end="")
            node = node.next_node


    def maximumvalue(self):
        current = self.head
        maximum = self.head.data
        if self.head == None:
            print("The list is empty.")
        else:
            while True:
                if (maximum < current.get_data()):
                    maximum = current.get_data
                    current = current.get_next
                if current == self.head:
                        break
        print("Maximum value in the list: ", str(maximum))

    def minimumvalue(self):
        current = self.head
        minimum = self.head.data
        if self.head == None:
            print("The list is empty.")
        else:
            while True:
                if (minimum > current.get_data()):
                    minimum = current.get_data
                    current = current.get_next
                if current == self.head:
                    break
        print("Minimum value in the list: ", str(minimum))
                 
       
while True:
    print("")
    print("+++++++++++++++++++++++++++++++++")
    print("1. Create List")
    print("2. Insert in beginning")
    print("3. Insert at the tail")
    print("4. Count element in the List")
    print("5. Enter Item to be deleted")
    print("6. Remove in beginning")
    print("7. Remove at tail")
    print("8. Display")
    print("9. Display element in reverse & forward order")
    print("10. Maximum value in the List")
    print("11. Minimum value in the List")
    print("12. Exit")
    print("+++++++++++++++++++++++++++++++++")  
    print("")


    choice = int(input("Enter your choice: "))

    if choice == 1:
        myLList = MyLList()
        print("The linked list has been created.")
        print("")

    elif choice == 2:
        while True:
            item = int(input("Enter number to add to the list: "))
            myLList.add(item)
            answer = input("Add more? Y/N")
            if answer == 'N':
                break
    
    elif choice == 3:
        while True:
            item = int(input("Enter number to be added to the end of the list: "))
            myLList.addtail(item)
            answer = input("Add more? Y/N")
            if answer == 'N':
                break
        
    elif choice == 4:
        print("Number of element(s) in the linked list: ",myLList.count())
        print("Linked list size : ",myLList.count())
        
    elif choice == 5:
        number = int(input("Enter number you want to delete: "))
        myLList.delete(number)

    elif choice == 6:
        print("Head is removed")
        myLList.removehead()

    elif choice == 7:
        print("Tail is removed")
        myLList.removetail()

    elif choice == 8:
        print("List of element(s):")
        myLList.printList()

    elif choice == 9:
        print("List of element(s) in forward order:")
        myLList.printList()
        print("\nList of element(s) in reversed order:")
        myLList.reverse()
        myLList.printList()


    elif choice == 10:
        myLList.maximumvalue()

    elif choice == 11:
        myLList.minimumvalue()

    else:
        break
