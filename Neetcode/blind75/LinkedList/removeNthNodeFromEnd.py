# Remove Node From End of Linked List
# Medium
# Topics
# Company Tags
# Hints
# You are given the beginning of a linked list head, and an integer n.

# Remove the nth node from the end of the list and return the beginning of the list.

# Example 1:

from GlobalFunctions import *
from typing import Optional

def removeNthFromEnd( head: Optional[ListNode], n: int) -> Optional[ListNode]:

    # /////////////////////// BASE APPROACH ////////////////////////

    if not head.next:
        return None
    
    # make the list circular
    lenght = 0
    temp = head
    while temp != None:
        temp = temp.next
        lenght += 1

    n =  lenght - n
    print("Index to remove: ", n)
    curr = head
    prev = ListNode(-999, curr)
    index = 0
    
    while curr != None:
        if index == n:
            prev.next = curr.next
            if n == 0:
                head = prev.next 
            break
        index += 1
        prev = prev.next
        curr = curr.next
    return head





h, n  = [1,2,3,4],2
head = makeLinkedList(h)
printList(removeNthFromEnd(head, n)) # Output: [1,2,4]

h ,n = [5], 1
head = makeLinkedList(h)
printList(removeNthFromEnd(head, n)) # Output: []

head,n = [1,2], 2
head = makeLinkedList(head)
printList(removeNthFromEnd(head, n)) #  Output: [2]

head,n = [1,2,3], 3
head = makeLinkedList(head)
printList(removeNthFromEnd(head, n)) #  Output: [2,3]
