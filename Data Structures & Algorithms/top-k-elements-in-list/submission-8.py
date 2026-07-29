class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        
        arr = [[] for i in range(max(d.values()))]

        for key, v in d.items():
            arr[v - 1].append(key)
        res = []
        for i in range(len(arr) -1, -1, -1):
            for j in arr[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return []