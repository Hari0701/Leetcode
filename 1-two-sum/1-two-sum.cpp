class Solution {
public:
    vector<int> twoSum(vector<int>& a, int k) {
		vector<pair<int,int>> v;
		int n=a.size(),x,y;
		for(int i=0;i<a.size();i++)
			v.push_back({a[i],i});
		sort(v.begin(),v.end());
		int i=0,j=n-1;
		while(i<j)
		{
			if(v[i].first+v[j].first==k)
			{
				x=v[i].second;
				y=v[j].second;
				break;                
			}
			if(v[i].first+v[j].first<k)
				i++;
			if(v[i].first+v[j].first>k)
				j--;
		}
		return {x,y};        
		}

};