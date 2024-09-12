class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int a,b,c,l;
        vector<int>v;
        l=nums.size();
        for (int i=0;i<l;i++)
        {
            a=target-nums[i];
            for(int j=i+1;j<l;j++)
            {
                if(nums[j]==a)
                {
                    b=i;
                    c=j;
                    break;
                }
            }
        }
        return vector<int> { b, c };
    }
};
