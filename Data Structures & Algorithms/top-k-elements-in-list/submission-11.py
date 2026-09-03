class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        res = [[] for i in range(len(nums))]
        for i, j in freq.items():
            res[j -1].append(i)
        
        r = []
        for i in range(len(res) -1, -1 , -1):
            for j in res[i]:
                r.append(j)
                if len(r) == k:
                    return r
        return r