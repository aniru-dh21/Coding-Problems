Question:
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]
Constraints:
- The number of nodes in the list is in the range [0, 300].
- -100 <= Node.val <= 100
- The list is guaranteed to be sorted in ascending order.

Solution:
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null){
            return null;
        }   
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode temp = dummy;
        while(temp.next != null && temp.next.next != null)
        {
            if(temp.next.val == temp.next.next.val)
            {
                int value = temp.next.val;
                while(temp.next != null && temp.next.val == value)
                {
                    temp.next=temp.next.next;
                }
            }
            else
            {
                temp = temp.next;
            }
        }
        return dummy.next;
    }
}
