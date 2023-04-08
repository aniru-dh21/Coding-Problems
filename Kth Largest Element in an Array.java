class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());
        for(int i:nums){
            queue.add(i);
        }
        int q = 1;
        while(q!=k)
        {
            queue.poll();
            q++;
        }
        return queue.poll();
    }
}
