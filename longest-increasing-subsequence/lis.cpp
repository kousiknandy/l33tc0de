class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> dp(nums.size(), 1);
        int maxlen = 1;
        for (int i = 1; i < nums.size(); i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    dp[i] = std::max(dp[i], dp[j]+1);
                    maxlen = std::max(maxlen, dp[i]);
                }
            }
        }
        return maxlen;
    }
};
