class node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1
        
    
    def pop(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = self.head
        while temp.next != None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
        if self.length == 0:
            self.head = 0
            self.tail = 0
        return temp.value
    
    def prepend(self,value):
        new_node = node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
        return True
    
    def pop_First(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        self.length -=1
        if self.length == 0:
            self.tail = None
        return temp.value
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp 
    
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        if index <0 or index >= self.length:
            return False
        if index == self.length:
            return self.append(value)
        if index == 0:
            return self.prepend(value)
        temp = self.get(index-1)
        new_node = node(value)
        new_node.next = temp.next
        temp.next = new_node
        self.length+=1
        return True
    
    def remove(self,index):       
        if index == self.length:
            return self.pop()
        if index == 0:
            return self.pop_First()
        prev = self.get(index-1)
        temp = self.get(index)
        prev.next = temp.next
        temp.next = None
        self.length-=1
        return temp
            

    def reverse(self):
        temp = self.head
        self.head = self.tail 
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            




my_Linked_List = LinkedList(0)
my_Linked_List.append(1)
my_Linked_List.append(7)
my_Linked_List.append(3)
my_Linked_List.print_list()
print("*****************")
my_Linked_List.remove(2)
my_Linked_List.print_list()


        
        


    
        