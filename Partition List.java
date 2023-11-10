Question:
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:
Input: head = [2,1], x = 2
Output: [1,2]
Constraints:
- The number of nodes in the list is in the range [0, 200].
- -100 <= Node.val <= 100
- -200 <= x <= 200

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
    public ListNode partition(ListNode head, int x) {
        ListNode dummy = new ListNode(-1);
        ListNode temp1 = dummy;
        ListNode dummy1 = new ListNode(-1);
        ListNode temp2 = dummy1;
        ListNode current = head;
        while(current!=null)
        {
            if(current.val < x)
            {
                temp1.next = current;
                temp1 = temp1.next;
            }
            else{
                temp2.next = current;
                temp2 = temp2.next;
            }
            current = current.next;
        }
        temp2.next = null;
        temp1.next = dummy1.next;
        return dummy.next;
    }
}
