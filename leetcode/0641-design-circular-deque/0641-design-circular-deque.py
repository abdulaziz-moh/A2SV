class Node:
    def __init__(self, number, nextp = None, prev = None):
        self.num = number
        self.next = nextp
        self.prev = prev

class MyCircularDeque:

    def __init__(self, k: int):
        self.count = 0
        self.k = k
        self.head = None
        self.front = None

    def insertFront(self, value: int) -> bool:
        if self.count >= self.k:
            return False

        newnode = Node(value)
        if self.count == 0:
            self.head = newnode
            self.front = newnode
            
        else:
            newnode.prev = self.front
            self.front.next = newnode
            self.front = newnode
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.count >= self.k:
            return False

        newnode = Node(value)
        if self.count == 0:
            self.head = newnode
            self.front = newnode
            
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.count == 0:
            return False
        if self.count == 1:
            temp = self.head
            self.head = None
            self.front = None
            del temp
        else:
            temp = self.front
            self.front = self.front.prev
            self.front.next = None
            temp.prev = None
            del temp
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.count == 0:
            return False
        if self.count == 1:
            temp = self.head
            self.head = None
            self.front = None
            del temp
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            del temp
        self.count -= 1
        return True

    def getFront(self) -> int:
        if self.count == 0:
            return -1
        return self.front.num

    def getRear(self) -> int:
        if self.count == 0:
            return -1
        return self.head.num

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getfront()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()