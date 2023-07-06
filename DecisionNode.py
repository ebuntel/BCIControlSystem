

class DecisionNode():

    '''
    For initializing the head node of a ControlTree, use:
    '''
    def __init__(self):
        self.ID = None                  # String
        self.content = None
        self.parent = None              # DecisionNode
        self.children = []              # List of DecisionNodes

    '''
    For initializing a non-head node of a ControlTree, use:
    '''
    def __init__(self, content, parent):
        self.ID = None                  # String
        self.content = content
        self.parent = None              # DecisionNode
        self.children = []              # List of DecisionNodes
