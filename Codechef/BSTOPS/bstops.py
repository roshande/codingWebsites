class Node:
    def __init__(self, val, pos):
        self.val = val
        self.left = None
        self.right  = None
        self.pos = pos

class BST:
    def __init__(self):
        self.root = None

    def __init__(self, num):
        self.root = Node(num ,1)

    def insert(self, num):
        if self.root is None:
            self.root = Node(num, 1)
            return 1
        new_node = self.root
        while True:
            if num > new_node.val:
                if new_node.right is None:
                    new_pos = 2* new_node.pos +1
                    new_node.right = Node(num,new_pos)
                    break
                new_node = new_node.right
            elif num < new_node.val:
                if new_node.left is None:
                    new_pos = 2* new_node.pos
                    new_node.left = Node(num, new_pos)
                    break
                new_node = new_node.left
        return new_pos

    def delete(self, num):
        if self.root is None:
            return None
        new_node = self.root
        while True:
            if new_node.val == num:
                return 


