def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i<oldSize else None  for i in range(size)]

class queue:
    def __init__(self,size = 5):
        self.tab = [None for _ in range(size)]
        #self.curr_size = 0
        self.first_id = 0
        self.end_id = 0

    def is_empty(self):
        if all(x is None for x in self.tab):
            return True
        else:
            return False
        
    def peek(self):
        return self.tab[self.first_id]
    
    def dequeue(self):

        if self.is_empty():
            return None
        if self.first_id + 1 == self.get_size():
            result = self.tab[self.first_id]
            self.tab[self.first_id] = None    
            self.first_id = 0

        else:
            result = self.tab[self.first_id]
            self.tab[self.first_id] = None    
            self.first_id +=1
        return result
        
    def enqueue(self, input):
        if self.end_id == self.get_size() and self.tab[0] == None: #when cycle
            self.end_id = 0
            self.tab[self.end_id] = input
            self.end_id +=1
        
        elif self.end_id == self.get_size() and self.tab[0] != None: # when cycle and table is full
            latest_size = self.get_size()
            self.tab = realloc(self.tab,2*latest_size)
            for i in range(0,latest_size):
                self.tab[i+latest_size] = self.tab[i]
                self.tab[i] = None
            self.end_id = 0
            self.tab[self.end_id] = input
            self.end_id +=1
            self.first_id = latest_size

        elif self.end_id == self.first_id and not self.is_empty(): # when save meet read
            latest_size = self.get_size()
            self.tab = realloc(self.tab,2*latest_size)
            for i in range(self.first_id,latest_size):
                self.tab[i+latest_size] = self.tab[i]
                self.tab[i] = None
            self.tab[self.end_id] = input
            self.end_id +=1
            self.first_id += latest_size
        else:
            self.tab[self.end_id] = input
            self.end_id +=1

    def show_tab(self):
        return [i for i in self.tab]
    
    def __str__(self):
        result = "["
        if self.first_id < self.end_id:
            for i in range(self.first_id, self.end_id):
                if self.tab[i] is not None:
                    result += f"{self.tab[i]} "
        elif self.first_id > self.end_id:
            for i in range(self.first_id, self.get_size()):
                if self.tab[i] is not None:
                    result += f"{self.tab[i]} "
            for i in range(self.end_id):
                if self.tab[i] is not None:
                    result += f"{self.tab[i]} "
        return str(result.strip() + "]")
    
    def get_size(self):
        return len(self.tab)
    



def main():
    que = queue()

    for x in range(1,5):
        que.enqueue(x)

    print(que.dequeue())
    print(que.peek())
    print(que)

    for x in range(5,9):
        que.enqueue(x)
    
    print(que.show_tab())

    for _ in range(que.get_size()):
        result = que.dequeue()
        if result == None:
            break
        print(result)
     
    print(que)
  
  

if __name__ == '__main__':
    main()
