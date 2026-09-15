class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        st = {}
        for x in s:
            st[x] = st.get(x,0) + 1
        tt = {}
        for x in t:
            tt[x] = tt.get(x,0) + 1

        if len(tt) != len(st): return False
        for x in tt:
            if tt[x] != st.get(x,0) : return False
        

        return True

        