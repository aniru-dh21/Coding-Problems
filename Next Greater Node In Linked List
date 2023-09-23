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
    public int[] nextLargerNodes(ListNode head) {
        List<Integer> L = new ArrayList<>();
        Stack<Integer> S = new Stack<>();
        ListNode curr = head;
        int count = 0;
        while(curr != null){
            count++;
            L.add(curr.val);
            curr = curr.next;
        }
        int ans[] = new int[count];
        for(int i=L.size()-1;i>=0;i--) {
            while(!S.isEmpty() && S.peek()<=L.get(i)){
                S.pop();
            }
            if(S.isEmpty()){
                ans[i] = 0;
            } else {
                ans[i] = S.peek();
            }
            S.push(L.get(i));
        }
        return ans;
    }
}
