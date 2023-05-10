import random
import time
import copy

class Element():
    def __init__(self,prior, dane = None) -> None:
        self.__prior = prior
        self.__dane = dane
       

    def __lt__(self,other):
        return self.__prior <= other.__prior

    def __gt__(self,other):
        return self.__prior >= other.__prior

    def __str__(self) -> str:
        return f'{self.__prior} : {self.__dane}'

class selection_sort():
    
    def __init__(self,to_sort = None, show = False) -> None:
            self.tab = to_sort
            self.size = len(to_sort)
    

    def sort_swap(self):
        work_list = copy.deepcopy(self.tab)
        for i in range(len(work_list)-1):
            mn_id = i

            for j in range(i+1,len(work_list)):
                if work_list[j] < work_list[mn_id]:
                    mn_id = j
            work_list[i], work_list[mn_id] = work_list[mn_id],work_list[i]

        self.tab = work_list
    
    def sort_shift(self):
        work_list = copy.deepcopy(self.tab)
        for i in range(len(work_list)-1):
            mn_id = i
            for j in range(i+1,len(work_list)):
                if work_list[j] < work_list[mn_id]:
                    mn_id = j
            to_shift = work_list.pop(mn_id)
            work_list.insert(i,to_shift)

        self.tab = work_list

    def print_tab(self):
        print ('{', end=' ')
        print(*self.tab[:self.size], sep=', ', end = ' ')
        print( '}')
    


def main():
    #### TEST 1
    tab1 = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    tab2 = []
    for x in tab1:
        tab2.append(Element(x[0],x[1]))
    test_list1 = selection_sort(tab2)
    test_list2 = selection_sort(tab2)
    
    #SWAP
    # algorytm niestabilny
    test_list1.sort_swap()
    test_list1.print_tab()
    
    #SHIFT
    # algorytm stabilny
    test_list2.sort_shift()
    test_list2.print_tab()
 

    ### TEST 2
    test_list = []
    for _ in range(10000):
        test_list.append(int(random.random() * 100))
    test_list_copy = copy.deepcopy(test_list)  
    
    #SWAP
    t_start = time.perf_counter()
    test = selection_sort(test_list)
    test.sort_swap()
    t_stop = time.perf_counter()
    print("Czas obliczeń swap:", "{:.7f}".format(t_stop - t_start))
    
    #SHIFT
    t_start = time.perf_counter()
    test = selection_sort(test_list_copy)
    test.sort_shift()
    t_stop = time.perf_counter()
    print("Czas obliczeń shift:", "{:.7f}".format(t_stop - t_start))

    #sortowanie przez kopcowanie jest zdecydowanie szybsze niż metody swap lub shift. W pojedynku shift oraz swap, nieco wolniejsza jest metoda swap.

if __name__ == '__main__':
    main()