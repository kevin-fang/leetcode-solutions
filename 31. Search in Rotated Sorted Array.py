from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        while low <= high:
            mid = (low + high) // 2
            print(low, high, mid, nums[mid])
            if target == nums[mid]:
                return mid
            elif nums[low] <= nums[mid]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else: # target > nums[mid]
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

x = Solution()
print(x.search([7, 0, 1, 2, 4, 5], 0))