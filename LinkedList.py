class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def insertstart(self, data):
        self.size = self.size + 1
        newnode = Node(data)

        if not self.head:
            self.head = newnode
        else:
            newnode.nextNode = self.head

    def remove(self, data):
        if self.head is None:
            return

        self.size = self.size - 1

        currentnode = self.head
        previousnode = None

        while currentnode.data != data:
            previousnode = currentnode
            currentnode = currentnode.nextNode

        if previousnode is None:
            self.head = currentnode.nextNode
        else:
            previousnode.nextNode = currentnode.nextNode

    # O(1) good
    def size(self):
        return self.size

    # O(n) not good
    def size2(self):
        actualnode = self.head
        size = 0

        while actualnode is not None:
            size += 1
            actualnode = actualnode.nextNode

        return size

    def insertend(self, data):
        self.size = self.size + 1
        newnode = Node(data)
        actualnode = self.head

        while actualnode.nextNode is not None:
            actualnode = actualnode.nextNode

        actualnode.nextNode = newnode

    def traverselist(self):
        actualnode = self.head

        while actualnode is not None:
            print("%d " % actualnode.data)
            actualnode = actualnode.nextNode


# End
