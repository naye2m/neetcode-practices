class Solution:
    def isPalindrome(self, s: str) -> bool:

        # s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        l = len(s)
        st, e = 0, l - 1
        print("s/e:", st, e)

        while st < e:
            while not s[st].isalnum():
                st += 1
                print("s:", st, e)
                if st > e: return True

            while not s[e].isalnum():
                e -= 1
                print("e:", st, e)
                if st > e : return True

            print("c3", st, e, s[st], s[e])
            if s[st].lower() != s[e].lower():
                return False
            st += 1
            e -= 1


        return True
