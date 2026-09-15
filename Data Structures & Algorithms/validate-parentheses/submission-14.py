class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {']' : '[', ')' : '(', '}' : '{'}

        st = []

        for i in s:
            if i in closeToOpen:
                if st and st.pop() == closeToOpen[i]:
                    continue
                else:
                    return False
            else:
                st.append(i)
        return not st
