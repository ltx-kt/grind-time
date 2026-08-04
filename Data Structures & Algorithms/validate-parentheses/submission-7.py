class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        closeToOpen = {'}' : '{', ')' : '(', ']' : '['}

        for i in s:
            # st.append(i)
            if i in closeToOpen:
                if st and st[-1] == closeToOpen[i]:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)
        return not st