class Solution {
    public:
        int removeDuplicates(vector<int>& nums) {
            vector<int> uniqueNums;
            int counts = 0;
            for(int i = 0; i< nums.size(); i++){
                if(!count(uniqueNums.begin(), uniqueNums.end(), nums[i])){
                    uniqueNums.push_back(nums[i]);
                    counts += 1;
                }
                else{
                    nums.erase(nums.begin()+ i);
                    i--;
                }
            }
            return counts;
        }
    };