from src.data_structures.linked_list import ListNode


class Solution:
    def mergeTwoLists(self, a: ListNode | None, b: ListNode | None) -> ListNode | None:
        match (a, b):
            case (an, None):
                return an
            case (None, bn):
                return bn
            case (an, bn):
                if an.val < bn.val:
                    an.next = self.mergeTwoLists(an.next, bn)
                    return an
                else:
                    bn.next = self.mergeTwoLists(an, bn.next)
                    return bn
            case _:
                return None
