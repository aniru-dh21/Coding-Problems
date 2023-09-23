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
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode dummy = new ListNode(0), curr;
        dummy.next = head;
        curr = dummy;
        while(head!=null && head.next!=null) {
            curr.next = head.next;
            head.next = head.next.next;
            curr.next.next = head;
            curr = curr.next.next;
            head = head.next;
        }
        return dummy.next;
    }
}
