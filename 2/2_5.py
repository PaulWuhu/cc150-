class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_sum(one,two):
    plus = 0
    temp = head = ListNode(0)
    while True:
        total = plus
        if one is not None:
                total += one.val
                one = one.next
        if two is not None:
                total += two.val
                two = two.next
        if total >=10:
            total -=10
            plus += 1
        else:
            plus = 0
        temp.next = ListNode(total)
        temp = temp.next
        if one is None and two is None:
            break

    if plus == 1:
        temp.next = ListNode(1)

    return head.next




def get_sum_backward(one,two):
    plus = 0
    temp = head = ListNode(0)
    while True:
        total = 0
        if one is not None:
                total += one.val
                one = one.next
        if two is not None:
                total += two.val
                two = two.next
        if total >=10:
            total -=10
            plus += 1
        else:
            plus = 0
        temp.next = ListNode(total+plus)
        temp = temp.next
        if one is None and two is None:
            break

    if plus == 1:
        temp.next = ListNode(1)

    return head.next
