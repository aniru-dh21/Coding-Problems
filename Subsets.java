class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> a = new ArrayList<>();
        f(0, nums, new ArrayList<>(), a);
        return a;
    }

    void f(int ind, int[] nums, List<Integer> subset, List<List<Integer>> a) {
        if (ind >= nums.length) {
            a.add(new ArrayList<>(subset));
            return;
        }
        subset.add(nums[ind]);
        f(ind+1,nums,subset,a);
        subset.remove(subset.size()-1);
        f(ind+1,nums,subset,a);
    }
}
