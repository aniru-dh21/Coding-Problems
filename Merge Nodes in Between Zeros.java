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
    public ListNode mergeNodes(ListNode head) {
        ListNode dummy = new ListNode(0);
        ListNode temp1 = dummy;
        ListNode temp2 = head.next;
        int sum = 0;
        while(temp2 != null)
        {
            if(temp2.val != 0)
            {
                sum += temp2.val;
            }
            else
            {
                temp1.next = new ListNode(sum);
                temp1 = temp1.next;
                sum = 0;
            }
            temp2 = temp2.next;
        }
        return dummy.next;
    }
}
