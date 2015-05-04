class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        loop = set([n])
        while n != 1:
            m = str(n)
            temp = reduce(lambda x,y: x + y, map(lambda x: int(x)*int(x), m))
            if (temp in loop):
                return False
            else:
                loop.add(temp)
                n = temp
        return True

if __name__ == '__main__':
    print Solution().isHappy(2);
    # print reduce(lambda x,y: int(x)*int(x) + int(y)*int(y), "82")