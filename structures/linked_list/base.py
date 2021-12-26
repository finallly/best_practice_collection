class LinkedListNode(object):

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f'{self.value} -> {self.next}'


class DoublyLinedListNode(object):

    def __init__(self, value=None, previous=None, next=None):
        self.value = value
        self.previous = previous
        self.next = next

    def __repr__(self):
        return f'{self.previous} -> {self.value} -> {self.next}'
