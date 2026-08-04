class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}
        
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        for i in nums:
            s[i] = s.get(i, 0) + 1
        
        for key, val in s.items():
            freq[val].append(key)
        for i in range(len(freq) -1 , 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return res
