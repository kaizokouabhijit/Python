class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    
    def create(self, data):
        
        if(self.head ==None):
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

        
    def addFront(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        




    def display(self):
        temp = self.head
        # print(f'The new head value is {temp.data} ')
        print('whole list')
        while(temp):
            print(temp.data)
            temp = temp.next
        




    def count(self):
        temp = self.head
        count = 0
        while(temp):
            count +=1
            temp = temp.next
        return count


    
    def addMiddle(self,pos, data):
        temp = self.head
        if(pos==0):
            raise Exception('Position cannot be zero')
        elif(pos == 1):
            self.addFront(data)
        else:
            position = 2
            temp = self.head
            while(position!=pos):
                temp = temp.next
                position+=1
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

        

    def deleteAtFirst(self):
        temp = self.head
        # print(f'The head value before deletion was {temp.data}')
        self.head = temp.next
        temp.next =None
        print(f"The deleted element is {temp.data}")

    def deleteAtLast(self):
        temp = self.head
        prev = None
        while(temp.next):
            prev = temp
            temp = prev.next
        prev.next = None
        print(f"The deleted element is {temp.data}")
        temp.data = None

    def deleteAtPos(self, pos):
        
        if(pos ==1):
            self.deleteAtFirst()
        
        elif pos == self.count():
            self.deleteAtLast()
        else:
            
                temp = self.head
                prev = None
                while(pos>1):
                    prev = temp
                    temp = prev.next
                    pos-=1
                prev.next = temp.next
                print(f"The deleted element is {temp.data}")
                temp.data = None
                temp.next = None

    def isEmpty(self):
        return (f"The statement 'the list is empty' is :{self.head ==None}")

    def elementExists(self, ele):
        temp = self.head
        while(temp.next):
            if(temp.data == ele):
                return (f'Element exists:{temp.data == ele}')
            else:
                temp = temp.next
        
        return (f'Element exists:{temp.data == ele}')

    def getIndex(self, ele):
        temp = self.head
        count = 0
        while(temp.next):
            if(temp.data == ele):
                return (f'Element was found at {count} index')
                
            else:
                temp = temp.next
                count+=1
        return ("Element not found")
    def getFirstOccurence(self, ele):
        return LinkedList.getIndex(self,ele)
    
    def getElementAtIndex(self, index):
        temp= self.head
        count = 0
        while(count !=index):
            temp = temp.next
            count+=1
        return (f"The element found at the index {index} is {temp.data}")

    def updateElemAtIndex(self, index, value):

        temp= self.head
        count = 0
        while(count !=index):
            temp = temp.next
            count+=1
        temp.data = value

    
    def getLastOccurence(self, ele):
        temp = self.head
        count = 0
        updated_index=0
        while(temp.next):
            if(temp.data == ele):
                updated_index = count
            
                temp = temp.next
                count+=1
            else:
                temp = temp.next
                count+=1
        if(temp.data == ele):
            updated_index = count
        return (f'the last occurence of the element was at {updated_index}')

    def LinearSearch(self, ele):
        return LinkedList.getIndex(self,ele)


    def BubbleSort(self):
        swap = 0
        if self.head != None:
            while(1):

                swap = 0
                tmp = self.head
                while(tmp.next != None):
                    if tmp.data > tmp.next.data:
                        
                        swap += 1
                        p = tmp.data
                        tmp.data = tmp.next.data
                        tmp.next.data = p
                        tmp = tmp.next
                    else:
                        tmp = tmp.next

                if swap == 0:
                    break
                else:
                    continue



    
    def selectionSort(self):
      
        temp = self.head
        
        while (temp):
            
            minn = temp
            remaining = temp.next
            
            
            while (remaining):
                if (minn.data > remaining.data):
                    minn = remaining
                
                remaining = remaining.next
                
            x = temp.data
            temp.data = minn.data
            minn.data = x
            temp = temp.next

    def InsertionSort(self):
        sorted = None
        curr = self.head
        while(curr!=None):
            next = curr.next
            sorted = self.sortedInsert(sorted, curr)
            curr = next
            self.head = sorted

    def sortedInsert(self, head, new_node):
        current = None
        if (head == None or (head).data >= new_node.data):
        
            new_node.next = head
            head = new_node
        
        else:
            current = head
            while (current.next != None and
                current.next.data < new_node.data):
            
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
            
        return head

    def partitionLast(self, start, end):
        if (start == end or start == None or end == None):
            return start
 
        pivot_prev = start
        curr = start
        pivot = end.data
        while (start != end):
            if (start.data < pivot):
 
                
                pivot_prev = curr
                temp = curr.data
                curr.data = start.data
                start.data = temp
                curr = curr.next
            start = start.next
        temp = curr.data
        curr.data = pivot
        end.data = temp
        return pivot_prev

    
    def Quicksort(self, start, end):
        
            
        if(start == None or start == end or start == end.next):
            return
            
        pivot_prev = self.partitionLast(start, end)
        self.Quicksort(start, pivot_prev)
        if(pivot_prev != None and pivot_prev == start):
            self.Quicksort(pivot_prev.next, end)
        elif (pivot_prev != None and pivot_prev.next != None):
            self.Quicksort(pivot_prev.next.next, end)

            
def take_input():
    data = input()
    return data
   
if __name__=='__main__':

    # list = LinkedList()

    # print("\tEnter 1 : insert data")
    # print("\tEnter 2 : Display")
    # print("\tEnter 3 : insert at First")
    # print("\tEnter 4 : insert in middle")
    # print("\tEnter 5 : delete at First")
    # print("\tEnter 6 : delete in last")
    # print("\tEnter 7 : delete as per given position")
    # print("\tEnter 11 : Check linked list is Empty or not")
    # print("\tEnter 12 : Check specified element exists in the given list or not")
    # print("\tEnter 13 : Get the index of first occurrence of given element")
    # print("\tEnter 14 : Get the element at given index")
    # print("\tEnter 15 : Update the element at the specified index ")
    # print("\tEnter 16 : Get last index of the occurrence of the specified element")
    # print("\tEnter 21: Linear Search")
    # print("\tEnter 22: Binary Search")
    # print("\tEnter 23: Bubble Sort")
    # print("\tEnter 24: Selection Sort")
    # print("\tEnter 25: Insertion Sort")
    # print("\tEnter 26: Quick Sort")
    # print("\tEnter 9 : Exit")
    # choice = int(input("Enter your choice"))
    # if(choice == 1):
    #     data = take_input()
    #     if(data!=-999):
            
    #         list.create(data)
    #         data = take_input()
    #     else:
    #         list.display()
    

    # print('this is main')
    llist = LinkedList()
    
    llist.create(1)
    llist.create(3)
    llist.create(4)
    llist.create(2)
    llist.create(10)
    llist.addFront(5)
    llist.addMiddle(1,6)
    llist.addMiddle(3,7)
    llist.addMiddle(4,8)
    # print(f'Total number of elements in the LinkedList is : {llist.count()}')
    # llist.deleteAtFirst()
    # llist.deleteAtLast()
    # llist.deleteAtPos(4)
    # print(llist.isEmpty())
    # print(llist.elementExists(9))
    # print(llist.getIndex(9))
    # print(llist.getFirstOccurence(6))
    # print(llist.getLastOccurence(6))
    # print(llist.LinearSearch(6))
    # print(llist.getElementAtIndex(3))
    # llist.updateElemAtIndex(3, 15)

    # llist.BubbleSort()
    # llist.selectionSort()
    llist.InsertionSort()
    # end = llist.head
    # while(end.next!=None):
    #     end = end.next
    # llist.Quicksort(llist.head, end)


    llist.display()

    
    
