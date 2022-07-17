class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int sum,start,end;
        vector<vector<int>>triplets;
        sort(nums.begin(),nums.end());
        
        for(int i = 0;i< nums.size() - 2; i++){
            
            if(i==0 || nums[i]!=nums[i-1]){
            start = i + 1;
            end = nums.size() - 1;
                
            while(start < end){
                sum = nums[i] + nums[start] + nums[end];
                if(sum == 0){
                    triplets.push_back({nums[i], nums[start], nums[end]});
                    
                        while(start<end && nums[start]==nums[start+1]){
                            start++;
                        }
                        while(start<end && nums[end]==nums[end-1]){
                            end--;
                        }
                    
                        start++;
                        end--;
                }
                
                else if(sum>0){
                        end--;
                    }
                else{
                        start++;
                    }
                }
            }
            }
        return triplets;
    }
};