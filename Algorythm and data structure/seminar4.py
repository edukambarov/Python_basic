class Node:
    def __init__(self, value, left = None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        res = f'значение нашего узла: {self.value}'
        # if self.left and self.right:
        #     res = f'значение нашего узла: {self.value}, значения левого: {self.left.value}, значение правого: {self.right.value}' 
        if self.left:
            res +=  f' значение левого: {self.left.value}'
        if self.right:
            res +=  f' значение правого: {self.right.value}'            
        return res
    
class Tree:
    def __init__(self, root = None):
        self.root = root

    def search(self, node, data, parent = None):
        if node == None or data == node.value:              
            return node, parent      
        if data > node.value:             
            return self.search(node.right, data, node)
        if data < node.value:            
            return self.search(node.left, data, node)
        
    def add_node(self, value):
        res = self.search(self.root, value)
        if res[0] is None:
            new_node = Node(value)
            if value > res[1].value:
                res[1].right = new_node
            else:
                res[1].left = new_node
        else:
            print('Ой все, такое значение уже есть')

    def delete_node(self,value):
        res = self.search(self.root,value)
        if res[0]:
            res[0] = 


        


node_1 = Node(15)
tree_1 = Tree(node_1)
print(tree_1.search(node_1,15))
print(node_1.right)

tree_1.add_node(16)
print(node_1.right)
print(node_1)
print(tree_1.search(node_1, 16))


tree_1.add_node(17)
tree_1.add_node(10)
tree_1.add_node(20)
tree_1.add_node(12)
tree_1.add_node(25)
print(node_1.left)
