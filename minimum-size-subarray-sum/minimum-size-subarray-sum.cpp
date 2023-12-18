class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int l = 0, r = 0, s = nums[0], d = nums.size() + 1;
        while (r < nums.size()) {
            if (s >= target) {
                d = min(d, r - l + 1);
                if (d == 1) return 1;
                s -= nums[l];
                l++;
            } else {
                r++;
                if (r >= nums.size()) break;
                s += nums[r];
            }
        }
        return d <= nums.size() ? d : 0;
    }
};
