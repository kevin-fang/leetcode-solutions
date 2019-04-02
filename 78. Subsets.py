class Solution(object):
        
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        combinations = []
        combinations.append([])
        for n in nums:
            for i in range(len(combinations)):
                subset = combinations[i][:]
                subset.append(n)
                combinations.append(subset)
                
        return combinations
