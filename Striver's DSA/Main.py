import LinkedList

# switcher = {
#     1: LinkedList.create(data),
#     2: tuesday,
#     3: wednesday,
#     4: thursday,
#     5: friday,
#     6: saturday,
#     7: sunday
#     }

# def switch(choice):
#     return switcher.get(choice)()


list = LinkedList()

print("\tEnter 1 : insert data")
print("\tEnter 2 : Display")
print("\tEnter 3 : insert at First")
print("\tEnter 4 : insert in middle")
print("\tEnter 5 : delete at First")
print("\tEnter 6 : delete in last")
print("\tEnter 7 : delete as per given position")
print("\tEnter 11 : Check linked list is Empty or not")
print("\tEnter 12 : Check specified element exists in the given list or not")
print("\tEnter 13 : Get the index of first occurrence of given element")
print("\tEnter 14 : Get the element at given index")
print("\tEnter 15 : Update the element at the specified index ")
print("\tEnter 16 : Get last index of the occurrence of the specified element")
print("\tEnter 21: Linear Search")
print("\tEnter 22: Binary Search")
print("\tEnter 23: Bubble Sort")
print("\tEnter 24: Selection Sort")
print("\tEnter 25: Insertion Sort")
print("\tEnter 26: Quick Sort")
print("\tEnter 9 : Exit")
choice = int(input("Enter your choice"))
if(choice == 1):
    data = int(input("Enter the value you want to insert in LL: "))
    list.create(data)

list.display()


    


    

    

