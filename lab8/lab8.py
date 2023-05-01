
class Element():
    def __init__(self,prior, dane = None) -> None:
        self.__prior = prior
        self.__dane = dane
       

    def __le__(self,other):
        return self.__prior <= other.__prior

    def __ge__(self,other):
        return self.__prior >= other.__prior

    def __str__(self) -> str:
        return f'{self.__prior} : {self.__dane}'

class Heap():
    
    def __init__(self,to_sort = None) -> None:
        if to_sort is not None:
            self.tab = to_sort
            self.size = self.get_size()
            self.initial_sort()
        else:
            self.tab = []
            self.size = 0

    def initial_sort(self):
        last_id = self.parent(self.get_size()-1)
        end = True
        self.print_tree(0,0)
        for i in range(- last_id, 1):
            i = i * (-1)
            self.repair(i)
        # while end:
        #     #self.print_tab()
        #     print(self.tab[last_id])
        #     print(self.tab[self.left(self.parent(last_id))])
        #     last_id = self.parent(last_id)
        #     self.repair(last_id)
        #     self.repair(self.left(self.parent(last_id)))
        #     if last_id == 1:
        #         end = False

        for _ in range(self.get_size()):
            self.dequeue()


    def __str__(self) -> str:
        pass

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
        
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[0]
        
    def left(self,idx):
        return 2*idx+1

    def right(self,idx):
        return 2*idx+2

    def parent(self,idx):
        return (idx - 1)//2
        
    def get_size(self):
        return len(self.tab)
    
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            self.tab[0], self.tab[self.size-1] = self.tab[self.size-1], self.tab[0]
            if self.size > 1:
                self.repair()
            

    def enqueue(self, prior, dane):
        if self.is_empty():
            self.tab.append(Element(prior,dane))
            self.size +=1
        else:
            if self.size == self.get_size(): ## extend table 
                self.tab.append(Element(prior,dane))
                self.size += 1
                self.repair(self.get_size()-1)
            else: ## add element to the last empty index
                self.tab[self.size] = Element(prior,dane)
                self.repair(self.size-1)
                self.size += 1

    def repair(self,idx = 0):
        if idx: #start from end (enqueue mclsethod)
            if self.tab[self.parent(idx)] <= self.tab[idx]:
                while self.tab[self.parent(idx)] <= self.tab[idx] and idx != 0:
                    self.tab[self.parent(idx)], self.tab[idx] = self.tab[idx], self.tab[self.parent(idx)]
                    idx = self.parent(idx)
        else: #start from top (dequeue method)
            while self.left(idx) <= self.size-1 and self.right(idx) <= self.size-1:
                if self.tab[idx] <= self.tab[self.left(idx)] and self.tab[self.left(idx)] >= self.tab[self.right(idx)]:
                    self.tab[self.left(idx)], self.tab[idx] = self.tab[idx], self.tab[self.left(idx)]
                    idx = self.left(idx)
                elif self.tab[idx] <= self.tab[self.right(idx)] and self.tab[self.left(idx)] <= self.tab[self.right(idx)]:
                    self.tab[self.right(idx)], self.tab[idx] = self.tab[idx], self.tab[self.right(idx)]
                    idx = self.right(idx)
                else:
                    break
            if idx == self.size - 2 and  self.tab[idx] <= self.tab[self.size - 1]:
                    self.tab[self.size - 1], self.tab[idx] = self.tab[idx], self.tab[self.size - 1]     
            

    def print_tab(self):
        print ('{', end=' ')
        print(*self.tab[:self.size], sep=', ', end = ' ')
        print( '}')

    def print_tree(self, idx, lvl):
        if idx<self.size:           
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)           
            self.print_tree(self.left(idx), lvl+1)



def main():
    tab1 = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    tab2 = []
    for x in tab1:
        tab2.append(Element(x[0],x[1]))
    kopiec1 = Heap(tab2)
    kopiec1.print_tab()
    kopiec1.print_tree(0,0)



if __name__ == '__main__':
    main()