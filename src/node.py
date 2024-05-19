import random


class Node:
    """
    Initializes a node with resource r. If r equals None, then it is a place for a city.
    """

    node_count = 0

    def __init__(self, r):
        self.resource = r
        dice_values = [12, 2, 1, 1, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11]
        random.shuffle(dice_values)
        self.value = 0
        if self.resource in [
            "Forest",
            "Pasture",
            "Fields",
            "Hills",
            "Mountains",
            "Desert",
        ]:
            self.value = dice_values[0]
        self.id = Node.node_count
        Node.node_count += 1
        # self.next = None
        # self.owner = None
        # self.building_type = None  # 'settlement', 'city', or None
        # self.adjacent_resources = []

    """
    Methods meant for adding or removing resource cards from players hands
    """

    # def insertAtEnd(self, r):
    #     newNode = Node(r)
    #     if self.head is None:
    #         self.head = newNode
    #         return

    #     currentNode = self.head
    #     while currentNode.next:
    #         currentNode = currentNode.next

    #     currentNode.next = newNode

    # def removeFirstNode(self):
    #     if self.head == None:
    #         return

    #     self.head = self.head.next

    # def deleteResource(self, r):
    #     currentNode = self.head
    #     if currentNode.r == r:
    #         self.removeFirstNode()
    #         return
    #     while currentNode is not None and currentNode.next.data != r:
    #         currentNode = currentNode.next

    #     if currentNode is None:
    #         return
    #     else:
    #         currentNode.next = currentNode.next.next

    def __str__(self):
        return (
            "Id: "
            + str(self.id)
            + " Resource: "
            + str(self.resource)
            + "  |  "
            + "Value: "
            + str(self.value)
        )
