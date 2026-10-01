class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        l = [[] for i in range(len(nums))]

        for key, val in d.items():
            l[val - 1].append(key)
        
        res = []
        for i in range(len(l) - 1, -1 , -1):
            for j in l[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return res