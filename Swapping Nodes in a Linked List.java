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
    public ListNode swapNodes(ListNode head, int k) {
        ListNode n1 = head;
        ListNode n2 = head;
        for (int i = 0; i < k - 1; i++) {
            n1 = n1.next;
        }
        ListNode curr = n1;
        while (curr.next != null) {
            n2 = n2.next;
            curr = curr.next;
        }
        int temp = n1.val;
        n1.val = n2.val;
        n2.val = temp;
        return head;
    }
}
