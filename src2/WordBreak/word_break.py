'''
Given a string s and a dictionary of words dict, 
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak_old(self, s, dict):
        if s in dict:
            return True
        print "----------------"
        for i in range(1, len(s)):
            print s[:i], ":|:", s[i:]
            if self.wordBreak(s[:i], dict) and self.wordBreak(s[i:], dict):
                return True
        return False

    def wordBreak(self, s, dict):
        sLen = len(s)
        charsInDict = [False] * (sLen)

        for i in range(0, sLen):
             charsInDict[i] = s[:i+1] in dict
             if charsInDict[i] is False:
                for j in range(0, i):
                    if charsInDict[j] is True:
                        if s[j+1:i+1] in dict:
                            charsInDict[i] = True
        return charsInDict[sLen-1]

if __name__ == '__main__':
    print Solution().wordBreak("leetcode", dict = ["leet", "code"])
    print Solution().wordBreak("goalspecial", dict = ["go","goal","goals","special"])
    print Solution().wordBreak("bccdbacdbdacddabbaaaadababadad", \
        ["cbc","bcda","adb","ddca","bad","bbb","dad","dac","ba","aa","bd",\
        "abab","bb","dbda","cb","caccc","d","dd","aadb","cc","b","bcc","bcd",\
        "cd","cbca","bbd","ddd","dabb","ab","acd","a","bbcc","cdcbd","cada",\
        "dbca","ac","abacd","cba","cdb","dbac","aada","cdcda","cdc","dbc","dbcb",\
        "bdb","ddbdd","cadaa","ddbc","babb"])