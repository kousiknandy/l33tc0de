class Solution {
    bool vowel(char c) {
        std::unordered_set<char> vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'};
        return vowels.contains(c);
    }

public:
    string reverseVowels(string s) {
        int l = 0;
        int r = s.length()-1;
        while (l < r) {
            while (l < r && !vowel(s[l])) l++;
            while (r > l && !vowel(s[r])) r--;
            if (l==r) break;
            auto t = s[l];
            s[l] = s[r];
            s[r] = t;
            l++;
            r--;
        }
        return s;
    }
};
