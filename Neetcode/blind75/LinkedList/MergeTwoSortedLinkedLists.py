# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

# The new list should be made up of nodes from list1 and list2.

from typing import Optional
from GlobalFunctions import *




def mergeTwoLists( h1: Optional[ListNode], h2: Optional[ListNode]) -> Optional[ListNode]:
        


        head = ListNode(-999)
        curr = head

        while h1 is not None and h2 is not None:
                
                if h1.val < h2.val:
                        curr.next = h1
                        h1 = h1.next
                        curr = curr.next

                else:
                        curr.next = h2
                        h2 = h2.next
                        curr = curr.next

        if h1 is not None:
                curr.next = h1
        elif h2 is not None:
                curr.next = h2

        return head.next




list1=[-9,3]
list2=[5,7]
head1 = makeLinkedList(list1)
head2 = makeLinkedList(list2)
printList(mergeTwoLists(head1, head2)) # Output: [-9,3,5,7]


# ================================================================


# list1, list2 = [1,2,4], [1,3,5]
# head1 = makeLinkedList(list1)
# head2 = makeLinkedList(list2)
# # printList(head1)
# # printList(head2)

# printList(mergeTwoLists(head1, head2)) # output Output: [1,1,2,3,4,5]

# ================================================================

# list1, list2 = [], [1,2]
# head1 = makeLinkedList(list1)
# head2 = makeLinkedList(list2)
# printList(mergeTwoLists(head1, head2)) # Output: [1,2]

# # ================================================================

# list1, list2  = [],  []
# head1 = makeLinkedList(list1)
# head2 = makeLinkedList(list2)
# printList(mergeTwoLists(head1, head2))  # Output: []
