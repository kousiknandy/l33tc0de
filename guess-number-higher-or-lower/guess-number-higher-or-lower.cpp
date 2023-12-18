/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int current_guess = 0;
        int tryme = 0x40000000;
        while (tryme) {
            auto res = guess(current_guess + tryme);
            if (res == 0) return current_guess + tryme;
            if (res > 0 ) current_guess += tryme;
            tryme /= 2;
        }
        return current_guess;
    }
};
