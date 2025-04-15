class Solution {
public:
    bool isPalindrome(int x) {
        string strx = std::to_string(x);
        string reversedx = strx;
        std::reverse(reversedx.begin(), reversedx.end());
        if (strx == reversedx)
            return true;
        else
            return false; 
    }
};