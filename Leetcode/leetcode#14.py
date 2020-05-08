class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Compare prefix at the same address
        # O(len_of_string * num_of_string)
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)

        for index, element in enumerate(s1):
            if element != s2[index]:
                return s1[:index]
            
        return s1