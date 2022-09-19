class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = len(s)
        j = 0
        all_longest = 0
        longest = 0
        check = list()
        while(j < i):
            if s[j]  not in check:
                check.append(s[j])
                j = j +1
                longest += 1
            else:
                pos = check.index(s[j])
                check = check[pos+1:] + [s[j]]
                j = j + 1
                if longest > all_longest:
                    all_longest = longest
                longest = longest - (pos+1) + 1

        if longest > all_longest:
            all_longest = longest
                
        return all_longest
