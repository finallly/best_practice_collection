from typing import Union, Any, Optional

from .base import LinkedListNode


def linked_list_generator(lst: list) -> LinkedListNode:
    buff = LinkedListNode(lst.pop(0))
    head = buff

    for value in lst:
        node = LinkedListNode(value)
        buff.next = node
        buff = buff.next

    return head


class SingleLinkedListMethods(object):

    def has_cycle(self, node: LinkedListNode) -> Union[bool, Any]:
        turtle = node
        hare = node

        while hare and hare.next:
            turtle = turtle.next
            hare = hare.next.next

            if turtle == hare:
                return turtle

        return False

    def detect_cycle(self, node: LinkedListNode) -> Optional[LinkedListNode]:
        if not node or not node.next:
            return None

        intersection = self.has_cycle(node)

        if not intersection:
            return None

        while intersection != node:
            node = node.next
            intersection = intersection.next

        return node

    def remove_rom_end(self, node: LinkedListNode, number: int) -> LinkedListNode:
        slow = node
        fast = slow

        for _ in range(number):
            fast = fast.next

        if not fast:
            return node.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return node

    def reverse_list(self, head: LinkedListNode) -> Optional[LinkedListNode]:
        last = None

        while head:
            buff = head
            head = head.next
            buff.next = last
            last = buff

        return last

    def remove_elements(self, head: LinkedListNode, value: int) -> Optional[LinkedListNode]:
        dummy = LinkedListNode(next=head)
        curr, prev = head, dummy

        while curr:
            if curr.val == value:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next

    def rotate_right(self, head: LinkedListNode, offset: int) -> Optional[LinkedListNode]:
        root = head
        length = 0

        while root:
            length += 1
            root = root.next

        iterations = offset % length
        root = head
        copy = root
        prev = None

        for _ in range(iterations):
            while root.next:
                prev = root
                root = root.next

            prev.next = None
            root.next = copy
            copy = root

        return root
