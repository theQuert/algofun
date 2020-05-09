class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Compare prefix at the same address
        # O(len_of_string * num_of_string)
        # We only have to do with the max. and min element in a lit, that's why choosing min, max.
    """
    # Method 1
        if not strs: return ""
        
        s1 = min(strs)
        s2 = max(strs)

        for index, element in enumerate(s1):
            if element != s2[index]:
                return s1[:index]
        return s1 
    """
        if not strs: return ""
        # zip: convert str to list
        ss = list(map(set, zip(*strs)))
        res = ""
        for index, element in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res