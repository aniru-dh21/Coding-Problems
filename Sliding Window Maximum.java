class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> queue = new ArrayDeque<>();
        int j = 0;
        int L[] = new int[nums.length-k+1];
        int i = 0;
        for(i=0; i<k; i++)
        {
            while(!queue.isEmpty() && nums[i] >= nums[queue.peekLast()])
            {
                queue.removeLast();
            }
            queue.addLast(i);
        }
        for(int index=i; index<nums.length; index++)
        {
            L[j++] = nums[queue.peek()];
            while(!queue.isEmpty() && queue.peek() <= index-k)
            {
                queue.removeFirst();
            }
            while(!queue.isEmpty() && nums[index]>=nums[queue.peekLast()])
            {
                queue.removeLast();
            }
            queue.addLast(index);
        }
        L[j] = nums[queue.peek()];
        return L;
    }
}
