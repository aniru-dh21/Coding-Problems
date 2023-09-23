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
    public ListNode removeZeroSumSublists(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        int p = 0;
        ListNode curr = dummy;
        Map<Integer, ListNode> mp = new HashMap<>();
        mp.put(p, dummy);
        while(curr != null) {
            p += curr.val;
            mp.put(p, curr);
            curr = curr.next;
        }
        p = 0;
        curr = dummy;
        while(curr != null) {
            p += curr.val;
            curr.next = mp.get(p).next;
            curr = curr.next;
        }
        return dummy.next;
    }
}
