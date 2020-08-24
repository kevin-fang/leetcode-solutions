from collections import defaultdict
class Solution(object):
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        words = defaultdict(lambda: [])
        
        for i in strs:
            words["".join(sorted(i))].append(i)
            
            
        results = []
        for i in words.keys():
            results.append(words[i])
            
        return results
