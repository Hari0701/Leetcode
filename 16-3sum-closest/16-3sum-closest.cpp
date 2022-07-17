class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int sum =  nums[0] + nums[1] + nums[2], dupsum, start, end;
        int closest = abs(nums[0] + nums[1] + nums[2] - target);
        sort(nums.begin(),nums.end());
        
        for(int i = 0;i< nums.size() - 2; i++){
            if(i == 0 || (i>0 && nums[i]!= nums[i-1])){
                
            start = i + 1;
            end = nums.size() - 1;
                
            while(start < end){
                dupsum = nums[i] + nums[start] + nums[end];
                if(dupsum == target) return target;
                
                if(abs(dupsum - target) < closest){
                    sum = nums[i] + nums[start] + nums[end];
                    closest = abs(sum - target);
                    
                    while(start<end && nums[start] == nums[start+1]) start++;
                    while(start<end && nums[end] == nums[end-1]) end--;
                }             
                if(dupsum > target){
                        end--;
                    }
                else{
                        start++;
                    }
                }
            }
        }
        
        return sum;
    }
};