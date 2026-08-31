# 5. 最长回文子串
# https://leetcode.cn/problems/longest-palindromic-substring/
# 思路：枚举每个位置作为中心，向两端扩散；奇数长度以 i 为中心，偶数长度以 i,i+1 为中心。


class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=len(s)
        res=""
        for i in range(l):
            #找回文串的难点在于，回文串的的长度可能是奇数也可能是偶数，
            #解决该问题的核心是从中心向两端扩散的双指针技巧。
            #如果回文串的长度为奇数，则它有一个中心字符；
            #如果回文串的长度为偶数，则可以认为它有两个中心字符。所以我们可以先实现这样一个函数：
            s1=self.getPalindrome(s,i,i)
            s2=self.getPalindrome(s,i,i+1)
            if len(s1)>len(res):
                res=s1
            if len(s2)>len(res):
                res=s2
        return res

    #在 s 中寻找以 s[l] 和 s[r] 为中心的最长回文串
    def getPalindrome(self, s: str, lo:int,hi:int) -> str:
        l=len(s)
        while lo>=0 and hi<l and s[lo]==s[hi]:
            lo-=1
            hi+=1
        return s[lo+1:hi]


if __name__ == "__main__":
    sol = Solution()

    assert sol.longestPalindrome("babad") in ("bab", "aba")
    assert sol.longestPalindrome("cbbd") == "bb"
    assert sol.longestPalindrome("a") == "a"
    assert sol.longestPalindrome("ac") in ("a", "c")

    print("all tests passed")
