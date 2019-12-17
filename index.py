#traverse

# O(N), linear time complexity

def insertEnd(self, data):
    self.size = self.size + 1;
    newNode = Node(data);
    actualNode = self.head;

    while actualNode.nextNode is not None:
        actualNode = actualNode.nextNode;

    actualNode.nextNode = newNode;

def traverseList(self):
    actualNode = self.head;

    while actualNode is not None:
        print("%d " % actualNode.data);
        actualNode = actualNode.nextNode;