class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod_list = []
        right_prod_list = []
        curr_product = 1
        for num in nums:
            curr_product *= num
            left_prod_list.append(curr_product)

        curr_product = 1
        for num in nums[::-1]:
            curr_product *= num
            right_prod_list.append(curr_product)

        output = [1] * len(nums)
        for i in range(len(nums) - 2):
            j = i + 1
            output[j] = left_prod_list[j - 1] * right_prod_list[-j - 2]

        output[0] = right_prod_list[-2]
        output[-1] = left_prod_list[len(nums) - 2]

        return output
