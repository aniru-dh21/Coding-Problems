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
    public ListNode sortList(ListNode head) {
        ListNode temp = head;
        int count = 0;
        while(temp != null)
        {
            count++;
            temp = temp.next;
        }
        temp = head;
        int L[] = new int[count];
        count = 0;
        while(temp!=null)
        {
            L[count++] = temp.val;
            temp = temp.next;
        }
        temp = head;
        Arrays.sort(L);
        count = 0;
        while(temp!=null)
        {
            temp.val = L[count++];
            temp = temp.next;
        }
        return head;
    }
}
