# 567. 字符串的排列
# https://leetcode.cn/problems/permutation-in-string/
# 思路：滑动窗口（同 76 题模板），窗口合法时收缩，若临界点窗口长度恰为 len(s1) 说明是排列。
# 注：原代码漏了 defaultdict 的 import，此处补上。

from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need=Counter(s1)
        window=defaultdict(int)

        lo=hi=0
        valid=0
        while hi<len(s2):
            c=s2[hi]
            hi+=1

            if c not in need:
                continue

            #进行窗口的一系列更新
            window[c]+=1
            if window[c]==need[c]:
                valid+=1

            #不断收缩左窗口
            while valid==len(need):
                d=s2[lo]
                if d in need:
                    #d为即将移出窗口的元素
                    if window[d]==need[d]:
                        valid-=1
                        if len(s1)==hi-lo:
                            return True

                    #Todo:别忘了这里!
                    #进行窗口的一系列更新
                    window[d]-=1

                lo+=1

        return False


if __name__ == "__main__":
    sol = Solution()

    assert sol.checkInclusion("ab", "eidbaooo") is True
    assert sol.checkInclusion("ab", "eidboaoo") is False
    assert sol.checkInclusion("a", "a") is True
    assert sol.checkInclusion("adc", "dcda") is True
    assert sol.checkInclusion("abc", "ab") is False
    assert sol.checkInclusion("aab", "eidbaaoo") is True
    assert sol.checkInclusion("aab", "eidbaoao") is False

    print("all tests passed")
