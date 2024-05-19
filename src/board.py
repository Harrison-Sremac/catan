from node import Node
from edge import Edge


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
        biomes = ["Forest", "Pasture", "Fields", "Hills", "Mountains", "Desert"]
        dice_values = [12,2,1,1,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11]

        

    def generate_tile(self):  
        self.nodes.append(Node("Ore"))
        for _ in range(6):
            self.nodes.append(Node(None))
        for i in range(1, 7):
            self.edges.append(Edge(self.nodes[0], self.nodes[i]))
        self.edges.append(Edge(self.nodes[1], self.nodes[2]))
        self.edges.append(Edge(self.nodes[2], self.nodes[3]))
        self.edges.append(Edge(self.nodes[3], self.nodes[4]))
        self.edges.append(Edge(self.nodes[4], self.nodes[5]))
        self.edges.append(Edge(self.nodes[5], self.nodes[6]))
        self.edges.append(Edge(self.nodes[6], self.nodes[1]))

    def __str__(self):
        s = "nodes:\n"
        for i in range(len(self.nodes)):
            s += "Index " + str(i) + " " + str(self.nodes[i]) + "\n"
        s += "edges\n"
        for i in range(len(self.edges)):
            s += "Index " + str(i) + " " + str(self.edges[i]) + "\n"
        return s
