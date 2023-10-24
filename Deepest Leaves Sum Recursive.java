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
    int sum = 0;
    public int deepestLeavesSum(TreeNode root) {
        int d = depth(root);
        LSum(root, d, 1);
        return sum;
    }

    public int depth(TreeNode root) {
        if (root == null) 
        return 0;
        return Math.max(depth(root.left), depth(root.right))+1;
    }

    public void LSum(TreeNode root, int depth, int curr) {
        if (root != null) 
        {
            if (curr == depth)
            {
                sum += root.val;
            }
            LSum(root.left, depth, curr+1);
            LSum(root.right, depth, curr+1);
        }
    }
}
