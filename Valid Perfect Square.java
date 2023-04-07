class Solution {
    public boolean isPerfectSquare(int num) {
        long min = 0;
        long max = num;

        while(min <= max){
            long mid = min + (max-min)/2;
            if(mid * mid == num) 
            {
                return true;
            }
            else if (mid * mid > num) 
            {
                max = mid - 1;
            }
            else {
                min = mid + 1;
            }
        }
        return false;
    }
}
