
from typing import Tuple, List

class linked_list:
    
    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None

    def add(self, input: Tuple):
        new = Node(input, self.head)
        self.head = new

    def append(self, input: Tuple):
        new_end = Node(input)
        if self.is_empty():
            self.head = new_end
        else:
            x = self.head
            while x.next != None:
                x = x.next
            x.next = new_end
    
    def lenght(self):
        counter = 1
        x = self.head
        while x.next != None:
            x = x.next
            counter += 1
        return counter


    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def show_nodes(self): 
        pivot = self.head
        result = "-> " + ''.join(str(pivot.data))
        while pivot.next != None:
                pivot = pivot.next
                result += '\n'+ "-> " + "".join(str(pivot.data))
        return result
        

    def remove(self):
        if self.is_empty() != True:
            self.head.prev = None
            self.head = self.head.next


    def remove_end(self):
        if self.is_empty() != True:
            x = self.head   
            for _ in range(self.lenght()-2):
                x = x.next
            x.next = None


    def get(self):
        if self.is_empty() != True:
            return self.head.data


class Node:

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    

def main():
    
  
    dane = [('AGH', 'Kraków', 1919),
             ('UJ', 'Kraków', 1364),
             ('PW', 'Warszawa', 1915),
             ('UW', 'Warszawa', 1915),
             ('UP', 'Poznań', 1919),
             ('PG', 'Gdańsk', 1945)]

    uczelnie = linked_list()

    uczelnie.append(dane[0])
    uczelnie.append(dane[1])
    uczelnie.append(dane[2])
    uczelnie.add(dane[3])
    uczelnie.add(dane[4])
    uczelnie.add(dane[5])

    print(uczelnie.show_nodes())
  
    print(uczelnie.lenght())

    uczelnie.remove()
    print(uczelnie.get())
 
    uczelnie.remove_end()
    print(uczelnie.show_nodes())

    uczelnie.destroy()
    print(uczelnie.is_empty())

    uczelnie.remove()
    uczelnie.remove_end()

if __name__ == '__main__':
    main()