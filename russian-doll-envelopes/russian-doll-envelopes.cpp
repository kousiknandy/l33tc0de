class Solution {
public:
    static bool comp_vex(vector<int> i, vector<int> j, int k) {
        int k1 = (k+1) % 2;
        return (i[k] == j[k] ? i[k1] < j[k1] : i[k] < j[k]);
    }
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        using namespace std::placeholders;
        vector<int> dp(envelopes.size(), 1);
        int maxlen = 1;
        std::sort(envelopes.begin(), envelopes.end(), std::bind(comp_vex, _1, _2, 0));
        
        for (int i = 1; i < envelopes.size(); i++) {
            for (int j = 0; j < i; j++) {
                if ((envelopes[j][0] < envelopes[i][0]) && (envelopes[j][1] < envelopes[i][1])) {
                    dp[i] = std::max(dp[i], dp[j]+1);
                    maxlen = std::max(maxlen, dp[i]);
                }
            }
        }
        return maxlen;
    }
};
