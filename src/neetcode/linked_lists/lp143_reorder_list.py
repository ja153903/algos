from src.data_structures.linked_list import ListNode


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        slow, fast = head, head

        # Use Fast and Slow Pointers here
        while slow and fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # here we want to make sure that we cut off
        # the first half
        half = slow.next if slow else None
        if slow and slow.next:
            slow.next = None

        curr, prev = half, None

        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next

        rev_head = prev

        while head:
            _next = head.next
            head.next = rev_head
            rev_head = _next

            head = head.next
