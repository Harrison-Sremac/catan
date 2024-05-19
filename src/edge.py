import node
import player


class Edge:
    """
    Initializes an edge connecting nodes u and v with no road
    """

    def __init__(self, u, v):
        self.u = u
        self.v = v
        self.road = None
        self.id = Edge.edge_count
        Edge.edge_count += 1

    """
    Adds a road for player p to the edge if it is a valid connection between 
    two valid spots for a city (i.e. not a city to resource connection)
    """
    edge_count = 0

    def add_road(self, p):
        assert self.u.resource == None and self.v.resource == None
        self.road = p.color

    def __str__(self):
        return (
            "Id: "
            + str(self.id)
            + " U: "
            + str(self.u)
            + " V: "
            + str(self.v)
            + " Road: "
            + str(self.road)
            + "  |  "
        )
