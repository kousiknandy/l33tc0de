class NumArray {
private:
    int *_cumsum;

public:
    NumArray(vector<int>& nums) {
        int s = 0;
        auto p = _cumsum = new int[nums.size()];
        for (int& n: nums) {
            s += n;
            *p++ = s;
        }    
    }
    
    int sumRange(int left, int right) {
        return *(_cumsum+right) - (left > 0 ? *(_cumsum+left-1) : 0);
    }

    /* WTF
     * >>> AddressSanitizer: alloc-dealloc-mismatch (operator new [] vs operator delete)
    ~NumArray() {
        delete _cumsum;
    }
    */
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */
