# delete a node from linked list when you only have this node

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_from_middle(mid):
    mid.val = mid.next.val
    mid.next = mid.next.next
