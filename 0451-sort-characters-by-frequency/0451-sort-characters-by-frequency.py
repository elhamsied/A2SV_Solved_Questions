class Solution:
    def frequencySort(self, s: str) -> str:
        freq_map = Counter(s)
        
        repeated_chars = []
        
        for char, freq in freq_map.items():
            repeated_chars.append(char * freq)
        
        repeated_chars.sort(key=lambda x: -len(x))
        
        result = ''.join(repeated_chars)
        
        return result