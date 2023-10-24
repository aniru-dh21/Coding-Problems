/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public ArrayList<Integer> l = new ArrayList<>();
    public TreeNode increasingBST(TreeNode root) {
        inorder(root);
        TreeNode dummy = new TreeNode(-1);
        TreeNode temp = dummy;
        for(int i = 0; i < l.size(); i++) {
            TreeNode temp1 = new TreeNode(l.get(i));
            dummy.left = null;
            dummy.right = temp1;
            dummy = dummy.right;
        }
        return temp.right;
    }
    public void inorder(TreeNode root) {
        if (root == null) return ;
        inorder(root.left);
        l.add(root.val);
        inorder(root.right);
        return ;
    }
}
