from src.data_structures.linked_list import ListNode


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev, curr = None, head

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
