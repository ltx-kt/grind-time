class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        closeToOpen = {']' : '[', ')' : '(', '}' : '{'}


        for i in s:
            if i in closeToOpen:
                if st and st.pop() == closeToOpen[i]:
                    continue
                else: 
                    return False
                
            st.append(i)
        return not st
