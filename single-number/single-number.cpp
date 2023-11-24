class Solution {
public:
    int singleNumber(vector<int>& nums) {
        return std::accumulate(nums.begin(),
            nums.end(),
            int(0),
            std::bit_xor<void>());
    }
};
