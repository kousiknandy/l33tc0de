class Solution {
    void counter(std::array<int, 26>& m, string& s) {
        for (char& c: s) m[c-'a']++; 
    }

    bool compare(const std::array<int, 26>&  s, const std::array<int, 26>&  t) {
        for (int i = 0; i < 26; i++) {
            if (t[i] != s[i]) return false;
        }
        return true;
    }
public:
    bool isAnagram(string s, string t) {
        std::array<int, 26> smap{}, tmap{};
        counter(smap, s);
        counter(tmap, t);
        return compare(smap, tmap);
    }
};
