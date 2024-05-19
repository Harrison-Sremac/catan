class Node:
    """
    Initializes a node with resource r. If r equals None, then it is a place for a city.
    """

    def __init__(self, data):
        self.resource = data
        # self.next = None
        self.owner = None
        self.building_type = None  # 'settlement', 'city', or None
        self.adjacent_resources = []
    
    """
    Methods meant for adding or removing resource cards from players hands
    """
    
    """
    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        currentNode = self.head
        while(currentNode.next):
            currentNode = currentNode.next

        currentNode.next = newNode

    def removeFirstNode(self):
        if(self.head == None):
            return
        
        self.head = self.head.next

    def deleteResource(self, data):
        currentNode = self.head
        if currentNode.data == data:
            self.removeFirstNode()
            return
        while currentNode is not None and currentNode.next.data != data:
            currentNode = currentNode.next
 
        if currentNode is None:
            return
        else:
            currentNode.next = currentNode.next.next
                  
    """
