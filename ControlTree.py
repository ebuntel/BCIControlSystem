from DecisionNode import DecisionNode

class ControlTree():
    def __init__(self):
        self.head = None
        self.size = 0
        self.position = self.head
        self.edges = {}
        self.edge_num = 0

    # From here on allows for manual control of the tree

    '''
    Manually creates a new node as a child of the current position node. 
    '''
    def manual_add_node(self, node):
        if self.head is None: # If the tree is empty
            self.head = node
            self.position = self.head
            self.size += 1
        else:                  # If the tree is not empty
            self.position.children.append(node)
            self.manual_add_edge(self.position, node)
            self.size += 1
        return node
    
    '''
    Manually moves the position to the specified node.
    '''
    def manual_move(self, node):
        self.position = node
        return node

    '''
    Manually resets the position to the head node.
    '''
    def manual_reset_position(self):
        self.position = self.head
        return self.head
    
    '''
    Manually adds an edge between two nodes.
    '''
    def manual_add_edge(self, node1, node2):
        if node1 and node2:
            self.edges[(node1, node2)] = 0
            self.edge_num += 1
        else:
            raise("Error: one of the entered nodes was None")

    '''
    Manually makes a decision regarding which child to move to using user input, then moves. 
    '''
    def manual_decide(self):
        counter = 0
        probabilities = []
        for child in self.position.children:
            print("Child #", counter, ": ", child.content)
            counter += 1
            probabilities.append(self.edges[(self.position, child)])
        
        print("Enter the number of the child you want to move to: ")
        choice = int(input())
        if(choice > len(probabilities)):
            raise("Error: choice was out of range")
        else:
            self.position = self.position.children[choice]
            return self.position
    
    # 