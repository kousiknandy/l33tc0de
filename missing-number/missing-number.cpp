class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int t1 = (nums.size() * (nums.size() + 1)) / 2;
        int t2 = 0;
        for (auto& n: nums) t2 += n;
        return t1-t2;
    }
};
