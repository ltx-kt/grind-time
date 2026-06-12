class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            print(st)
            if i in '[{(':
                st.append(i)
            if i in '}])':
                if not any(st):
                    return False
                if i == '}' and st.pop() != '{':
                    return False
                if i == ')' and st.pop() != '(':
                    return False
                if i == ']' and st.pop() != '[':
                    return False
        return not any(st)