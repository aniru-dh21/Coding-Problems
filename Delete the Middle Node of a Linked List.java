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
    public ListNode deleteMiddle(ListNode head) {
        ListNode temp = head;
        ListNode slow = head;
        ListNode fast = head;
        if(head.next == null)
        {
            head = head.next;
        }
        while(fast != null && fast.next != null)
        {
            slow = slow.next;
            fast = fast.next.next;
        }
        while(temp != null)
        {
            if(temp.next == slow){
                temp.next = temp.next.next;
            }
            temp = temp.next;
        }
        return head;
    }
}
