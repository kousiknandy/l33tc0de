class Solution {
public:
    string finalString(string s) {
        string l, r;
        bool inv = false;
        for (int i = s.length()-1; i >= 0; i--) {
            if (s[i] == 'i') {
                inv = !inv;
                continue;
            }
            if (inv) {
                l = l + s[i];
            } else {
                r = s[i] + r;
            }
        }
        return l + r;
    }
};
