class Solution {
public:
    string reverseOnlyLetters(string s) {
        int l = 0;
        int r = s.length()-1;
         while (l < r) {
            while (l < r && !isalpha(s[l])) l++;
            while (r > l && !isalpha(s[r])) r--;
            if (l==r) break;
            std::swap(s[l], s[r]);
            l++;
            r--;
        }
        return s;
    }
};
