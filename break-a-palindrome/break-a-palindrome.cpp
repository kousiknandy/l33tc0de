class Solution {
public:
    string breakPalindrome(string palindrome) {
        auto l = palindrome.size();
        if (1 == l) {
            return string("");
        }
        for(std::string::size_type i = 0; i < l; ++i) {
            if (palindrome[i] != 'a' && i != l/2) {
                palindrome[i] = 'a';
                return palindrome;
            }
        }
        palindrome[l-1] = 'b';
        return palindrome;
    }
};
