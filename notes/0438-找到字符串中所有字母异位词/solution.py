# 438. 找到字符串中所有字母异位词
# https://leetcode.cn/problems/find-all-anagrams-in-a-string/
# 思路：滑动窗口（76/567 同款模板），收缩临界点若窗口长度恰为 len(p)，记录左端点 lo。
# 注：原代码漏了 from typing import List，此处补上。

from collections import defaultdict, Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need=Counter(p)
        window=defaultdict(int)

        lo=hi=0
        valid=0
        res=[]

        while hi<len(s):
            c=s[hi]
            hi+=1

            if c not in need:
                continue

            #移入窗口，进行窗口的一系列更新
            window[c]+=1
            if window[c]==need[c]:
                valid+=1

            while valid==len(need):
                d=s[lo]

                if d in need:
                    #d要即将被移出窗口，先检查一下是否会对valid造成影响
                    if window[d]==need[d]:
                        valid-=1
                        #Todo:符合要求，才能更新答案，例如s=cbba,p=abc,就不属于，因为会多了一个b字符
                        if len(p)==hi-lo:
                            res.append(lo)

                    #移出窗口，进行窗口的一系列更新
                    window[d]-=1
                lo+=1
        return res


if __name__ == "__main__":
    sol = Solution()

    assert sol.findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert sol.findAnagrams("abab", "ab") == [0, 1, 2]
    assert sol.findAnagrams("cbba", "abc") == []
    assert sol.findAnagrams("a", "aa") == []
    assert sol.findAnagrams("aaaa", "aa") == [0, 1, 2]

    print("all tests passed")
