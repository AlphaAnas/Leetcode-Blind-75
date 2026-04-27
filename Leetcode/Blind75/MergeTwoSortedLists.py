
# Code
# Testcase
# Testcase
# Test Result
# 21. Merge Two Sorted Lists
# Easy
# Topics
# premium lock icon
# Companies
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.



class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

     
def mergeTwoLists(list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode(0)
        merged = head
        while list1 and list2:
             if list1.val <= list2.val:
                  merged.next = list1
                  list1 = list1.next
             else:
                  merged.next = list2
                  list2 = list2.next
             merged = merged.next
                            
        merged.next = list1 or list2

        return head.next
        












# print(mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4])) # Output: [1,1,2,3,4,4]
# print(mergeTwoLists(list1 = [], list2 = [])) # Output: []
# print(mergeTwoLists(list1 = [], list2 = [0])) # Output: [0]
