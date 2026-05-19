
from typing import Optional, List
from GlobalFunctions import *


def mergeTwoLists(list1, list2):

    curr = ListNode(-999)
    head = curr
    printList(list1)
    printList(list2)
    while list1 and list2:
        if list1.val < list2.val:
            head.next = list1
            head = list1
            list1 = list1.next
        else:
            head.next = list2
            head = list2
            list2 = list2.next

    if list1:
        head.next = list1
    elif list2:
        head.next = list2

    return head

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:


    # //////////////////////////////// Optimized /////////////////////// 
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return None
        for i in range(len(lists)):
            lists[i] = mergeTwoLists(lists[i], lists[i-1])

        print(lists)

        # /////////////////////////////// brute-force  ////////////////
        # final = []
        # for heads in lists:
        #      c = heads
        #      while c :
        #          final.append(c.val)
        #          c = c.next  
        # h = makeLinkedList(sorted(final))
        # return h
  


# //////////////////////////////////
def makeKlinkedLists(lists):
    l = []
    for list in lists:
        if len(list) > 0:
        
            l.append(makeLinkedList(list))
    return l

lists = [[1,2,4],[1,3,5],[3,6]]
l = makeKlinkedLists(lists)
printList(mergeKLists(l)) # Output: [1,1,2,3,3,4,5,6]


# lists = []
# l = makeKlinkedLists(lists)
# printList(mergeKLists(l)) # Output: []


# lists = [[]]
# l = makeKlinkedLists(lists)
# printList(mergeKLists(l)) # Output: []

