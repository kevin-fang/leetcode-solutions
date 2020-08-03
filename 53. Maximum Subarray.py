class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum > max_sum:
                max_sum = curr_sum
            if num < 0 and abs(num) > (curr_sum - num):
                curr_sum = 0
            print(curr_sum, max_sum)

        return max_sum
