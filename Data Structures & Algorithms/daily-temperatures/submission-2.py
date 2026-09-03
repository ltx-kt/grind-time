class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)):

            while st and temperatures[st[-1]] < temperatures[i]:
                l = st.pop()
                res[l] = i - l
            st.append(i)
        return res