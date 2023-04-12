class child_node():
    def __init__(self, key, data, left = None, right = None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right


class Tree():
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        def _insert_rec(node, key, data):
            if key == node.key:
                node.data = data
            if key < node.key:
                if node.left == None:
                    node.left = child_node(key, data)
                else:
                    _insert_rec(node.left, key, data)
            elif key > node.key:
                if node.right == None:
                    node.right = child_node(key,data)
                else:
                    _insert_rec(node.right, key, data)

        if self.root is None:
            self.root = child_node(key, data)
        else:
            node = self.root
            _insert_rec(node, key, data)

    def search(self, key):
        def search_rec(node, key):
            if node is None:
                return node
            if key == node.key:
                return node.data
            if key < node.key:
                return search_rec(node.left, key)
            elif key > node.key:
                return search_rec(node.right, key)
            else:
                return node

        if self.root is None:
            print("drzewo jest puste")
        else:
            node = self.root
            result = search_rec(node, key)
            return result

    def delete(self,key):
        
        def check_kids(node):
            if node.left is not None and node.right is not None:
                return (node.left, node.right)
            elif node.left is not None: 
                return (node.left,)
            elif node.right is not None: 
                return (node.right,)
            else:
                return ()
            
        def _delete_search(node, key):
            if node is None:
                return None, None
            if node.left is not None and key == node.left.key:
                return node, node.left
            if node.right is not None and key == node.right.key:
                return node, node.right
            if key < node.key:
                return _delete_search(node.left, key)
            elif key > node.key:
                return _delete_search(node.right, key)
            else:
                return None, None
            
        def _delete(parent, kid):
            #kid with no kids
            if not check_kids(kid):
                if kid == self.root: #root
                    self.root = None
                else:
                    if parent.left == kid:
                        parent.left = None
                    else:
                        parent.right = None
            #kid with two kids
            elif len(check_kids(kid)) == 2:
            
                temp_node = kid.right
                #2 nodes check first right node
                if not check_kids(temp_node):
                    if kid == self.root:
                        self.root = self.root.right
                    elif parent.left == kid:
                        temp_node.left = kid.left
                        parent.left = temp_node
                    else:
                        temp_node.left = kid.left
                        parent.right = temp_node
              
                else: #2 nodes wher lowest has kid
                    last_node = temp_node
                    if temp_node.left is not None:
                        while(temp_node.left != None):
                            last_node = temp_node
                            temp_node = temp_node.left
                            
                    if temp_node.right is None: #2 nodes wher lowest dont have right kid
                        if kid == self.root:
                            temp_node.left = kid.left
                            temp_node.right = kid.right
                            last_node.left = None  
                            self.root = temp_node
                        elif parent.left == kid:
                            temp_node.left = kid.left
                            temp_node.right = kid.right
                            parent.left = temp_node
                            last_node.left = None    
                        else:
                            temp_node.left = kid.left
                            temp_node.right = kid.right
                            parent.right = temp_node
                            last_node.left = None
                    else: #2 nodes wher lowest have right kid
                        if last_node.left is not None:
                           last_node.left = temp_node.right
                        if kid == self.root:
                            temp_node.left = kid.left
                            temp_node.right = kid.right
                            self.root = temp_node
                        elif parent.left == kid:
                            temp_node.left = kid.left
                            if temp_node == kid.right:
                                temp_node.right = kid.right.right
                            else:
                                temp_node.right = kid.right
                            parent.left = temp_node
                        else:
                            temp_node.left = kid.left
                            if temp_node.right == kid.right:
                                temp_node = kid.right.right
                            else:
                                temp_node.right = kid.right
                            
                            parent.right = temp_node

            #kid with one kid
            elif check_kids(kid)[0] == kid.left: #left kid
                if kid == self.root:
                    self.root = self.root.left
                elif parent.left == kid:
                    parent.left = kid.left
                else:
                    parent.right = kid.left
            else:
                if kid == self.root:
                    self.root = self.root.right
          
                elif parent.left == kid:
                    parent.left = kid.right
                else:
                    parent.right = kid.right
        
        
        if self.root is None:
            print("drzewo jest puste")
        else:
            if key == self.root.key:
                _delete(self.root,self.root)
            #check if if to delete id root
            else:
                node = self.root
                parent, to_delete  = _delete_search(node,key)
                if to_delete != None and parent != None:
                    _delete(parent,to_delete)
                else:
                    print("Nie ma takiego węzła")
            
            
        
    def height(self):
        def height_rec(node, count=0, remember=0):
            if node is not None:
                count += 1
        
                if count > remember: #getting highest value
                    remember = count

                remember = height_rec(node.left, count, remember)
                remember = height_rec(node.right, count, remember)
                count -= 1
            return remember
        return height_rec(self.root)
    


    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")
            
    def __print_tree(self, node, lvl):
            if node!=None:
                self.__print_tree(node.right, lvl+5)

                print()
                print(lvl*" ", node.key, node.data)
        
                self.__print_tree(node.left, lvl+5)


    def __str__(self):
        def str_rec(node, lst=None):
                if lst is None:
                    lst = []
                if node is not None:
                    str_rec(node.left, lst)
                    lst.append(node)
                    str_rec(node.right, lst)
                    return lst
        string = "["
        lst = str_rec(self.root)
        for el in lst:
            if el == lst[-1]:
                string += str(el.key) + ":" + str(el.data)
            else:
                string += str(el.key) + ":" + str(el.data) + ", "
        string += "]"
        return string


def main():

    tree = Tree()
    dic = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}

    for key, values in dic.items():
        tree.insert(key,values)

    tree.print_tree()
    print(tree)
    print(tree.search(24))
    tree.insert(20,"AA")
    tree.insert(6,"M")
    tree.delete(62)
    tree.insert(59,"N")
    tree.insert(100,"P")
    tree.delete(8)
    tree.delete(15)
    tree.insert(55,"R")
    tree.delete(50)
    tree.delete(5)
    tree.delete(24)
    print(tree.height())
    print(tree)
    tree.print_tree()



if __name__ == '__main__':
    main()