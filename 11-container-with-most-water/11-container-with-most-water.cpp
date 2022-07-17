class Solution {
public:
    int maxArea(vector<int>& height) {
        int pt1 = 0, pt2 = height.size() - 1;
        int maxArea = 0,area,length,width;
        while(pt2 > pt1){
            width = pt2 - pt1;
            area = width * min(height[pt1], height[pt2]);
            maxArea = max(maxArea, area);
            if(height[pt1] < height[pt2]){
                pt1++;
            }
          else{
                pt2--;
            }
        }
        return maxArea;
    }
};