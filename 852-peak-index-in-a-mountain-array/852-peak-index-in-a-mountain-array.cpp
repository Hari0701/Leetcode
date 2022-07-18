class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int peakidx;
        int maxpeak = 0;
        for(int i = 1; i< arr.size() - 1;i++){
            if(arr[i - 1] < arr[i] and arr[i] > arr[i + 1]){
                if(arr[i] > maxpeak){
                    maxpeak = arr[i];
                    peakidx = i;
                    i+= 1;
                }else{continue;} 
            }
        }
        return peakidx;
    }
};