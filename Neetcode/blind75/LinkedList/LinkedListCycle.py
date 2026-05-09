# Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

# There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.

# Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

# Note: index is not given to you as a parameter.

from GlobalFunctions import * 
from typing import Optional



def hasCycle(head: Optional[ListNode]) -> bool:
            

            # /////////////////////// two pointer approach O(1) space /////////////////////////////////////
            if head == None:
                return False
            
            slow = head
            fast = head

            while fast and fast.next :
                    
                slow = slow.next
                fast = fast.next.next
                
                if slow == fast:
                       return True


            return False

            #  ///////////////////////////////////////////////////////////////////////////////

            # /////////////////////////////// HASMAP APPROACH O(n) space //////////////////////
            if head == None:
                return False
            h = {}
            curr = head
            index = 0
            while curr.next != None:
                    
                    if curr.val in h:
                            return True
                    
                    h[curr.val] = index
                    curr = curr.next
                    index += 1

            return False

            # /////////////////////////////////////////////////////////////////////////////////////
                    


head = makeLinkedList([1,2,3,4])
newNode = ListNode(2, head)
head = newNode
print(hasCycle(head)) # output true
# head = makeLinkedList([1,2])
# print(hasCycle(head)) # output false
