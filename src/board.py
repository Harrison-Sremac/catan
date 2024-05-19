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
    
    def gen_board():
    # This function will print a random catan board this is useful
    # for creating the intial set up and for quickly making games
    # numbers will correlate to different biomes
    # there should be 19 tiles in Catan generated
        biomes = ['Forest', 'Pasture', 'Fields', 'Hills', 'Mountains', 'Desert']
  
