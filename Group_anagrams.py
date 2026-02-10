class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dic = {}
        for word in strs:
            anagram = "".join(sorted(word))
            if anagram in anagram_dic:
                anagram_dic[anagram].append(word)
            else:
                anagram_dic[anagram] = [word]
        return list(anagram_dic.values())
