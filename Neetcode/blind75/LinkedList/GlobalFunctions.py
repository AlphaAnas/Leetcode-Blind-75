class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def makeLinkedList(list):
    if len(list) == 0:
         return None
    head = ListNode(list[0]) 
    prev = head
    next = None
    for i in range(1, len(list)):
        next = ListNode(list[i])
        prev.next = next
        prev = next

    return head

def printList(head):
        if head is None:
             return []
        print("[")
        while head.next != None:
            print(head.val, end = ", ")
            head = head.next
      
        print(head.val)
        print(" ]")
