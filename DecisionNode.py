

class DecisionNode():

    '''
    For initializing the head node of a ControlTree, use:
    '''
    def __init__(self, content = None, parent = None):
        self.ID = None                  # String
        self.content = content
        self.parent = parent              # DecisionNode
        self.children = []              # List of DecisionNodes

    '''
    For manually setting the ID of a node, use:
    '''
    def _manual_set_ID(self, ID):
        self.ID = ID
        return ID
