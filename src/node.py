class Node:
    """
    Initializes a node with resource r. If r equals None, then it is a place for a city.
    """

    def __init__(self, r):
        self.resource = r
        if self.resource == None:
            self.city = None
        else:
            self.is_robber = False
