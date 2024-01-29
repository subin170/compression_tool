from typing import Any


class HuffManNode:
    def __init__(self, char, weight, left , right):
        self.char = char
        self.weight = weight
        self.left = left
        self.right = right


class HuffManTree:
    def __init__(self ):
        self.root: HuffManNode = None
        self.codes = defaultdict(str)  
        # self.tree = []


    def create_new_huff_Node(self, Heap):
        RootNode = Heap.pop()
        
        for Node in Heap:
            MinNode = Node.pop()
            NewNode = HuffManNode
            NewNode.weight = MinNode.value + RootNode.value
            NewNode.char = None
            self.tree.append(NewNode)
            RootNode = NewNode
        
