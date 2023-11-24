class Solution {
public:
    void counter(std::array<int, 26>& m, string& s) {
        for (char& c: s) m[c-'a']++; 
    }

    char compare(const std::array<int, 26>&  s, const std::array<int, 26>&  t) {
        for (int i = 0; i < 26; i++) {
            if (t[i] > s[i]) return char('a'+i);
        }
        return '0';
    }

    char findTheDifference(string s, string t) {
        std::array<int, 26> smap{}, tmap{};
        counter(smap, s);
        counter(tmap, t);
        return compare(smap, tmap);
    }
};
