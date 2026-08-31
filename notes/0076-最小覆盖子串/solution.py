# 76. 最小覆盖子串
# https://leetcode.cn/problems/minimum-window-substring/
# 思路：滑动窗口，need/window 两个计数表 + valid 计数已满足的字符种数；窗口合法时收缩左边界并更新答案。

#使用库
from collections import Counter,defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=Counter(t)
        window=defaultdict(int)

        #窗口是左开右闭s[lo,hi)
        lo=hi=0
        res=""
        res_len=len(s)+1 #不可能的数值
        l=len(s)
        #表示有多少个字符已经满足了条件
        valid=0

        while hi<l:
            #获取当前元素
            c=s[hi]
            #Todo:注意这里此时hi已经+1了，自然满足右开
            hi+=1

            if c not in need:
                continue

            #满足条件则增大右边窗口
            window[c]+=1
            # 进行窗口内数据的一系列更新
            if window[c]==need[c]:
                valid+=1

            #判断是否需要收缩左窗口
            while valid==len(need):
                #d是即将移出窗口的元素
                d=s[lo]

                if d in need:
                    #左窗口的字符是我们需要关注的
                    if window[d]==need[d]:
                        #左窗口字符即将要不满足答案了，先看看能不能更新答案
                        if res_len>hi-lo:
                            res_len=hi-lo
                            res=s[lo:hi]

                        valid-=1
                    #进行窗口内的一系列更新
                    window[d]-=1

                #左移动窗口
                lo+=1

        return res


if __name__ == "__main__":
    sol = Solution()

    assert sol.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert sol.minWindow("a", "a") == "a"
    assert sol.minWindow("a", "aa") == ""
    assert sol.minWindow("aa", "aa") == "aa"

    print("all tests passed")
