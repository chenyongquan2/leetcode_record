# 3. 无重复字符的最长子串
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/
# 思路：滑动窗口，右端吸收字符后若 window[c]>1 说明有重复，收缩左端直到把前一个 c 挤出窗口。

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window=defaultdict(int)
        lo=hi=0

        res=0

        while hi<len(s):
            c=s[hi]
            hi+=1

            #移入窗口，进行窗口的一系列更新
            window[c]+=1

            #判断是否需要收缩左窗口
            while window[c]>1:
                #错误写法
                #d=window[lo]
                d=s[lo]
                window[d]-=1
                lo+=1


            #这里是没有重复的
            res=max(res,hi-lo)

        return res


if __name__ == "__main__":
    sol = Solution()

    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    assert sol.lengthOfLongestSubstring("") == 0
    assert sol.lengthOfLongestSubstring("abba") == 2
    assert sol.lengthOfLongestSubstring("dvdf") == 3

    print("all tests passed")
