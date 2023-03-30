from src.data_structures.linked_list import ListNode


class Solution:
    def mergeTwoLists(self, a: ListNode | None, b: ListNode | None) -> ListNode | None:
        match (a, b):
            case (an, None) if an is not None:
                return an
            case (None, bn) if bn is not None:
                return bn
            case (an, bn) if an is not None and bn is not None:
                if an.val < bn.val:
                    an.next = self.mergeTwoLists(an.next, bn)
                    return an
                else:
                    bn.next = self.mergeTwoLists(an, bn.next)
                    return bn
            case _:
                return None
