# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node that acts as the starting point of the merged list.
        # This helps simplify the logic since we don't need to handle a special "first node" case.
        head = ListNode()
        curr = head  # 'curr' will always point to the last node of the merged list.

        # Traverse both lists until one of them becomes empty
        while list1 and list2:
            # Compare the current nodes of both lists
            if list1.val <= list2.val:
                # If list1's value is smaller (or equal), attach it to the merged list
                curr.next = list1
                list1 = list1.next  # Move to the next node in list1
            else:
                # Otherwise, attach list2's node to the merged list
                curr.next = list2
                list2 = list2.next  # Move to the next node in list2

            # Move the 'curr' pointer forward in the merged list
            curr = curr.next

        # At this point, one of the lists is empty.
        # Directly attach the remaining part of the non-empty list to the merged list.
        curr.next = list1 if list1 else list2
    
        # Return the merged list, skipping the dummy head node
        return head.next
