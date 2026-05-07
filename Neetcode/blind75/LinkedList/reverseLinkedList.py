# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverseList(self, head):
          pass

def printList(head):
      
        print("[")
        while head.next != None:
            print(head.val, end = ", ")
            head = head.next
      
        print(head.val)
        print(" ]")

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:

        # ///////////////////////// unoptimized version (takes 45 ms and 7.9mb) /////////////////////////

        prev = None
        curr = head

        while curr != None:
              nxt = curr.next
              curr.next = prev
              prev = curr
              curr = nxt
            
        return prev

        '''
        # //////////////////////// unoptimized version (takes 28ms and 8mb) ////////////////////////////
        if head == None:
              return []
        elif head.next == None: # only one element is same
              return head
        curr = head
        tail = curr
        while curr.next != None:
              curr = curr.next
        tail = curr
        
        # print(tail.val)

        # 1. store the next node
        # 2. current node next is null (for first node)
        # 3. Move to next node 
        # 4. Store its next node
        # 5. Set its next node to head
        # 6. Move to that next node
        # 7. Store its next node
        # 8. Set its next node to current node

        # ....

        # repeat step 6,7,8 until current node is tail
        h = head
        next = h.next
        h.next = None


        nnext = next.next
        next.next = head
        if nnext == None:
              return next # list had only two elements no need to go ahead
       
        prev = next 
        curr = nnext
        
        # printList(next) # till here we are on the second node and its next node is the head
        while curr != tail:
                nxt = curr.next # store the next node
                curr.next = prev # point to the previous node
                prev = curr
                curr = nxt

        tail.next = prev # last node points to 2nd last
     
        printList(tail)


        '''








n1 = ListNode(2)
head = ListNode(1, n1)

reverseList(head) # output [2,1]



# print(reverseList(head=None)) # output []
