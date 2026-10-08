class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        s = {'+', '-', '*', '/'}

        for i in tokens:
            if i in s:
                n2 = st.pop()
                n1 = st.pop()
                t = self.eval(n1, n2, i)
                st.append(t)
            else:
                st.append(int(i))
        return st[0]
        
    def eval(self, n1, n2, op):
        if op == "+":
            return n1 + n2
        elif op == "-":
            return n1 - n2
        elif op == "*":
            return n1 * n2
        elif op == "/":
            print(n1, n2)
            print(int(n1 / n2))
            print(n1 // n2)
            return int(n1 / n2)

