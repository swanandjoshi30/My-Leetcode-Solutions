# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val          # store the digit
#         self.next = next        # pointer to the next node

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to simplify result list construction
        dummy = ListNode()
        cur = dummy   # 'cur' will always point to the last node in the result list
        
        carry = 0  # initialize carry for addition
        
        # Loop until both lists are processed and no carry remains
        while l1 or l2 or carry:
            # Get current values from l1 and l2, or 0 if list is exhausted
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Add the two digits plus any carry from previous step
            val = v1 + v2 + carry
            
            # Update carry for the next step
            carry = val // 10
            
            # The digit to store in this node is remainder after dividing by 10
            val = val % 10
            
            # Create a new node with this digit and attach to result list
            cur.next = ListNode(val)
            
            # Move 'cur' pointer forward
            cur = cur.next
            
            # Move l1 and l2 pointers forward if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Return the next of dummy node, which is the head of the result list
        return dummy.next
