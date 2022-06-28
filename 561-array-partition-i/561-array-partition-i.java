class Solution {
    public int arrayPairSum(int[] nums) {
        int sum = 0;
      Arrays.sort(nums);
        for(int j = 0; j <nums.length; j +=2){
            sum += nums[j];
        }
        return sum;
    }
}