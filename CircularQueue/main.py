from ..LinkedList.main import LinkedList as LL

class MyCircularQueue:
    def __init__(self, k: int):
        self.list = LL()
        self.max_len = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.list.addAtTail(value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.list.deleteAtIndex(0)
        return True

    def Front(self) -> int:
        return self.list.getHead()

    def Rear(self) -> int:
        return self.list.getTail()

    def isEmpty(self) -> bool:
        return self.list.isEmpty()
        
    def isFull(self) -> bool:
        return self.max_len == self.list.length()