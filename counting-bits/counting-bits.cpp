class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> b_c;
        int l = 0;
        b_c.push_back(0);
        while (l < n) {
            vector<int> t;
            for (auto b: b_c) {
                t.push_back(1+b);
                if (++l == n) break;
            }
            b_c.insert(end(b_c), begin(t), end(t));
        }
        return b_c;
    }
};
