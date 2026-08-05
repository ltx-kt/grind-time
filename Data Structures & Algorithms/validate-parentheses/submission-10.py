class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        closeToOpen = {'}' : '{', ']' : '[', ')' : '('}

        for i in s:
            if st and i in closeToOpen:
                if st[-1] == closeToOpen[i]:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)
        print(st)
        return not st
                