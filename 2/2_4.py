# partition

# change the linked list so that all the node's value is smaller appear before the one thats later



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head,parition):
    l1 = ListNode()
    l2 = ListNode()

    while head:
        if head.val >= parition:
            l2.next = head
        else:
            l1.next = head
        head=head.next



# i have list of [10,2,30,3,4,5]
# parition is 4
# result [2,3,4,5,10,30] or some kind of formation like this
