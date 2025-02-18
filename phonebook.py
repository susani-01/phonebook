class Node:
    def __init__(self, name=" ",number=None):
       self.name = name
       self.number = number
       self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
        
    def Insert(self,name,number):
        new_node = Node(name,number)
        new_node.next = self.head
        self.head = new_node
        
    def View(self,name):
        current = self.head
        while current:
            if current.name==name:
                print(f"Phone Number for {name}: {current.number}")
                return 
            current = current.next
        print(f"{name} not found in the list.")

    def Update(self,name,new_number):
        contact = self.head
        while contact:
            if contact.name == name:
                contact.number = new_number
                print("Contact updated successfully!")
                return 
        
            contact = contact.next
        print("Contact '{name}' not found!")
        
    def Delete(self,name):
        if self.head is None:
            print("Phonebook is empty!")
            return 

        if self.head.name == name:
            self.head = self.head.next
            print("Contact deleted successfuly")
                
    def display(self):
        if self is None:
            print("Phonebook is empty!")
            return
        current = self.head
        while current is not None:
            print(f"Name: {current.name},phone Number: {current.number}")
            current = current.next
            print("_ _ _")
            
            
a_llist = LinkedList()
 
print('**********Menu***********')
print(" press [I] Insert Contact")
print(" press [V] View  Contact")
print(" press [U] Update Contact")
print(" press [D] Delete Contact")
print(" press [S] View all contact")
print(" press [X] Exit")

while True:
    ch=str(input("Enter your choice :"))
    if ch=='I' or ch== 'i': # to add a contact
        name = input("Enter your name: ")
        number = input("Enter your number: ")
        a_llist.Insert(name,number)
        print("Contact inserted successfully!")    
               
    elif ch=='V' or ch== 'v':
        name = input("Name you want to view:")
        a_llist.View(name)
    
    elif ch=='U' or ch== 'u':
         name = input("Enter the name of the number you want to update: ")   
         new_number = input("Enter the new number")
         a_llist.Update(name,new_number)        
        
    elif ch=='D' or ch=='d':
        name = input("Enter the name to be deleted: ")
        a_llist.Delete(name)
    elif ch=='S' or ch=='s':
        a_llist.display()
        
    elif ch=='X' or ch== 'x':
        break
        
    else :print("invalid option ")
    