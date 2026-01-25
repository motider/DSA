class Solution(object):
    def groupAnagrams(self, strs):
        x= []
        for i in range(len(strs)):
            y = sorted(strs[i])
            result = "".join(y)
            x.append(result)
        paired = [list(pair) for pair in zip(strs, x)]
        
        groups = {} 
        for i in paired:
            word = i[0]       
            sorted_key = i[1] 
            if sorted_key not in groups:
                groups[sorted_key] = []
            
            groups[sorted_key].append(word)
        final_result = list(groups.values())
        return final_result
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        