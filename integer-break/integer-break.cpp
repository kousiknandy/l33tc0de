class Solution {
public:
    int pow3(int x) {
        int y = 1;
        for (auto i = 0; i < x; i++) y*= 3;
        return y;
    }
    int integerBreak(int n) {
        auto dv = std::div(n, 3);
        if (n == 2) return 1;
        if (n == 3) return 2;
        if (dv.rem == 1) return pow3(dv.quot - 1) * 4;
        if (dv.rem == 2) return pow3(dv.quot) * 2; 
        return pow3(dv.quot);
    }
};
