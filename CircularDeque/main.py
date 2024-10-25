from ..LinkedList.main import MyLinkedList as LL

class MyCircularDeque:
    def __init__(self, k: int):
        self.list = LL()
        self.max_len = k
        
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.list.addAtHead(value)
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.list.addAtTail(value)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.list.deleteAtIndex(0)
        return True
        
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.list.deleteAtIndex(self.list.length()-1)
        return True

    def getFront(self) -> int:
        return self.list.getHead()

    def getRear(self) -> int:
        return self.list.getTail()

    def isEmpty(self) -> bool:
        return self.list.isEmpty()

    def isFull(self) -> bool:
        return self.max_len == self.list.length()