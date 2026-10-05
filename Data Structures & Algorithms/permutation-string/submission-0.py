class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = defaultdict(int)
        s2_freq = defaultdict(int)

        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len:
            return False

        for i in range(s1_len):
            s1_freq[s1[i]] += 1
            s2_freq[s2[i]] += 1

        if self.isPermutation(s1_freq, s2_freq):
            return True

        for i in range(1, s2_len - s1_len + 1):
            s2_freq[s2[i - 1]] -= 1
            s2_freq[s2[i + s1_len - 1]] += 1
            if self.isPermutation(s1_freq, s2_freq):
                return True
        
        return False
    
    def isPermutation(self, s1_dict, s2_dict):
        for key in s1_dict:
            if s1_dict[key] != s2_dict[key]:
                return False
        
        for key in s2_dict:
            if s2_dict[key] != s1_dict[key]:
                return False
        
        return True
