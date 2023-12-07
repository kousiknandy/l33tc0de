class Solution {
public:
    string convertToBase7(int num) {
        int base = 7;
        string r;
        bool negative = false;
        if (num == 0) return "0";
        if (num < 0) {
            negative = true;
            num = -num;
        }
        while (num) {
            int d = num % base;
            num /= base;
            r = char(d + '0') + r;
        }
        if (negative) {
            r = '-' + r;
        }
        return r;
    }
};
