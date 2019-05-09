#include <algorithm>
#include <iostream>
using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        for (size_t i = nums.size() - 1; i > 0; i--) {
            if (nums[i] > nums[i - 1]) {
                int minDiff = INT_MAX;
                int index = -1;
                for (size_t j = i; j < nums.size(); j++) {
                    int diff = nums[j] - nums[i - 1];
                    if (diff > 0 && diff <= minDiff) {
                        minDiff = diff;
                        //cout << "new mindiff: " << minDiff;
                        index = j;
                    }
                }
                //cout << "i - 1: " << i - 1 << ", index: " << index << ", mindiff: " << minDiff << endl;
                int tmpVal = nums[i - 1];
                nums[i - 1] = nums[index];
                nums[index] = tmpVal;
                reverse(nums.begin() + i, nums.end());
                return;
            }
        }
//cout << "Reverse normally" << endl;
        reverse(nums.begin(), nums.end());
    }
};
