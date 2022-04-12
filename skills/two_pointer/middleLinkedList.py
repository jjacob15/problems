class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
    def setNext(self, next):
        self.next = next
        return next

def middleNode(head):
    fast =  head
    slow = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
        
    return slow
            


if __name__ == "__main__":
    i = 1
    n = None
    h = None
    while i <= 5:
        if n is None:
            n = ListNode(i)
        else:
            n = n.setNext(ListNode(i))
        i +=1
    
    if middleNode(n).val == 3:
        print('pass')
    else:
        print('fail')

    # i = 1
    # n = None
    # while i <= 6:
    #     if n is None:
    #         n = ListNode(i)
    #     else:
    #         n.next = ListNode(i)
    #     i += 1
    # if middleNode(n).val == 4:
    #     print('pass')
    # else:
    #     print('fail')
