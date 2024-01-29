from typing import Any

class Node:
    def __init__(self, char, value):
        self.char = char
        self.value = value

    def __eq__(self, othernode):
        return self.char == othernode.char and self.value == othernode.value
    

class MinHeap:
    
    def __init__(self):
        self.heap = []
    
    def getparent_idx(self, i):
        return (i-1)//2
    
    def get_leftchild_idx(self, i):
        return 2*1 + 1
    
    def get_rightchild_idx(self, i):
        return 2*i + 2
    
    def get_lastindex(self):
        return len(self.heap) - 1

    def getNodeAt(self, i):
        if i > self.get_lastindex() or i < 0:
            return  None
        return self.heap[i]
    
    
    def bubbleup(self, Node):
        current_index = self.get_lastindex()
        while current_index > 0:
            current_node = self.getNodeAt(current_index)
            if current_node != Node:
                return
            
            parent_index = self.getparent_idx(current_index)
            parent_node = self.getNodeAt(parent_index)

            if parent_node.value > current_node.value:
                self.heap[parent_index], self.heap[current_index] = current_node, parent_node
                current_index = parent_index
            else:
                break
        

    def bubbledown(self, Node):
        current_index = 0
        while current_index < len(self.heap):
            root_node = self.getNodeAt(current_index)
            leftchild_index = self.get_leftchild_idx(current_index)
            rightchild_index = self.get_rightchild_idx(current_index)
            left_node = self.getNodeAt(leftchild_index)
            right_node = self.getNodeAt(rightchild_index)
            minchild_node = Node
            min_node_idx = -1
            if left_node.value <= right_node.value:
                minchild_node = left_node
                min_node_idx = leftchild_index
            else:
                minchild_node = right_node
                min_node_idx = rightchild_index
            
            if minchild_node.value < root_node.value:
                self.heap[min_node_idx], self.heap[current_index] = minchild_node, root_node
                current_index = min_node_idx
            else:
                break

    def pop(self):
        min_element = self.heap[0]
        self.heap[0] = self.getNodeAt(self.get_lastindex)
        del self.heap[-1] # last element delete 
        self.bubbledown()

        return min_element
        
    def insertnodes(self, dictionary):
        for Node in dictionary:
            self.heap.append(Node)
            self.bubbleup(Node)

a = [3,8,10,5,15,7]

# print(heapify(a))

# print(callingthefunc())
        
        
        
        
