class Solution {
public:
    string toHex(int num) {
        std::array<char, 16> hexdigits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};
        string output;
        uint hexnum;
        if (num == 0) return "0";
        if (num < 0) {
            hexnum = 4294967295 + num + 1;
        } else {
            hexnum = num;
        }
        while (hexnum) {
            output = hexdigits[hexnum % 16] + output;
            hexnum /= 16;
        }
        return output;
    }
};
