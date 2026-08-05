class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []

        for i in range(len(temperatures)):
            while st and st[-1][1] < temperatures[i]:
                idx, temp = st.pop()
                res[idx] = i - idx
            st.append((i, temperatures[i]))
        return res