from node import Node


class Board:
    """
    Initializes an empty game board
    """

    def __init__(self):
        self.nodes = []
        self.edges = []

    """
    Generates nodes and verticies for this instance
    """

    def generate(self):
        # modifiy nodes and edges
        for _ in range(6):
            self.nodes.append(Node(None))
        self.nodes.append(Node("ore"))
        # add edges
        return 0
