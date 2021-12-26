from typing import Union, Any, Optional

from .base import LinkedListNode


def linked_list_generator(lst: list) -> LinkedListNode:
    buff = LinkedListNode(lst.pop(0))
    head = buff

    for val in lst:
        node = LinkedListNode(val)
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
        fast = slow = node
        for _ in range(number):
            fast = fast.next

        if not fast:
            return node.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return node

    def reverse_list(self, head: Optional[LinkedListNode]) -> Optional[LinkedListNode]:
        last = None

        while head:
            buff = head
            head = head.next
            buff.next = last
            last = buff

        return last

    def remove_elements(self, head, val: int):
        dummy = LinkedListNode(next=head)
        curr, prev = head, dummy

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next
