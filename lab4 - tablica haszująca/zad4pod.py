class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class hashtable:
    def __init__(self, size, c1 = 1, c2 = 0) -> None:
        self.tab = [None for _ in range(size)]
        self.c1 = c1
        self.c2 = c2
    
    #zwraca indeks tablicy
    def get_key(self, input) -> int:
        N =  len(self.tab)
        if isinstance(input, str):
            sum = 0
            for x in input:
                sum += ord(x)
            return sum%N
        elif isinstance(input,int):
            return input%N
        else:
            raise ValueError

    def insert(self, key, value):
        id = self.get_key(key)
   
        if self.tab[id] == None or self.tab[id].key == key or self.tab[id] == "deleted":
            self.tab[id] = Element(key, value)
        else:
            id = self.resolve_collision(id,key)
            if id == None:
              
                print("lista pelna")
            else:
                self.tab[id] = Element(key, value)

    def resolve_collision(self, id, key):
        size = len(self.tab)
        for i in range(1,size+1):
            new_id = (id + self.c1*i + self.c2*(i**2))%size
            if self.tab[new_id] == None or self.tab[new_id] == "deleted" or self.tab[new_id].key == key:
                return new_id     
        return None
    
  
    def remove(self, key):
        remove_id = self.find_index(key)
        if remove_id is None:
       
            raise ValueError
        self.tab[remove_id] = "deleted"
        
   
    def search(self, key):
        result = self.find_index(key)
        if result is None:
   
            return "Nie ma danej o takim kluczu"
        else:
            return (self.tab[result].key,self.tab[result].value)
        
    
    def find_index(self,key):
        id = self.get_key(key)

        if self.tab[id] == None:
            return None
        else:
            size = len(self.tab)
            for i in range(1,size+1):
                new_id = (id +self.c1*i +self.c2*(i**2))%size
                if self.tab[new_id] == None or self.tab[new_id] == "deleted":
                    continue
                if self.tab[new_id].key == key:
                    return new_id
            return None



    def __str__(self) -> str:
        result = "{"
        for i in range(len(self.tab)):
            if self.tab[i] == None:
                result += "None:, "
            elif self.tab[i] == "deleted":
                result += "deleted:, "
            else:
                result += f"{str(self.tab[i].key)}: {str(self.tab[i].value)}, "
        result.strip()
        result += "}"
        return result
    
def testFunction1(size, c1, c2):
    tab = hashtable(size,c1,c2)
    keys = [1,2,3,4,5,18,31,8,9,10,11,12,13,14,15]
    values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for i in range(len(keys)):
        tab.insert(keys[i],values[i])
    print(tab)
    print(tab.search(5)) 
    print(tab.search(14))   
    tab.insert(5,"Z")
    print(tab.search(5))   
    tab.remove(5)  
    print(tab)
    print(tab.search(31)) 
    tab.insert('test',"W")
    print(tab)


def testFunction2(size, c1, c2):
    tab = hashtable(size,c1,c2)
 
    values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for i in range(len(values)):
        tab.insert(13 + (13 * i),values[i])
    print(tab)

def main():

    testFunction1(13,1,0)
  
    testFunction2(13,1,0)
  
    testFunction2(13,0,1)
  
    testFunction1(13,0,1)



if __name__ == '__main__':
    main()