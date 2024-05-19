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
        self.nodes.append(Node("Mountains"))
        # add edges
        return 0

    def gen_board(self):
        # This function will print a random catan board this is useful
        # for creating the intial set up and for quickly making games
        # numbers will correlate to different biomes
        # there should be 19 tiles in Catan generated
        for _ in range(3):
            self.nodes.append(Node("Mountains"))
        for _ in range(4):
            self.nodes.append(Node("Pasture"))
        for _ in range(4):
            self.nodes.append(Node("Forest")) 
        for _ in range(4):
            self.nodes.append(Node("Wheat"))
        for _ in range(3):
            self.nodes.append(Node("Hills"))
        self.nodes.append(Node("Desert"))
        for _ in range(54):
            self.nodes.append(Node(None))
        print(len(self.nodes))
        # Total edges: city to city edges: 72 + city to resource edges: 19*6
        i = 19 #first city node of 73 nodes total
        #Right Idea but doesnt workx!!! account for nodes next to multiple resources (loop through less than 19 multiple times for nodes next to 1, 2, 3 resources)
        for u in range(19):
            for _ in range(6):
                self.edges.append(Edge(u, 19))
                i += 1

        # for i in range(18,73):
        #     self.edges.append((Edge(i )))

        # self.edges.append(Edge(19, 20))
        # self.edges.append(Edge(19, 20))
        # self.edges.append(Edge(18, 19))
        # self.edges.append(Edge(18, 19))
        # self.edges.append(Edge(18, 19))
        # self.edges.append(Edge(18, 19))
        # self.edges.append(Edge(18, 19))
        # self.edges.append(Edge(18, 19))
        # self.edges.append(Edge(18, 19))
        # self.edges.append(Edge(18, 19))
        # self.edges.append(Edge(18, 19))
        # self.edges.append(Edge(18, 19))
        # self.edges.append(Edge(18, 19))
        # self.edges.append(Edge(18, 19))
        # self.edges.append(Edge(18, 19))
        # self.edges.append(Edge(18, 19))


        
        
    def generate_tile(self):
        self.nodes.append(Node("Forest"))
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
