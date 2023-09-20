class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def last_K_elements(head,k):
    if head is None:
        return None
    counter = 0
    slow = fast =head
    while counter<k and fast is not None:
        fast = fast.next
        counter += 1
    while fast:
        fast = fast.next
        slow = slow.next
    return slow
    # we need two different loop, and they are different by K
    # so the first one start then after K element the second one start
    #  then we get the last K element when first one stops
