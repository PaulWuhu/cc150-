# remove dupilicate from an unsorted linked list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove(head):
    maps = {}
    prev = None
    curr = head
    while curr:
        if curr.val in maps:
            prev.next = curr.next
        else:
            maps[curr.val] = 1
            prev = curr
        curr = curr.next

    return head
