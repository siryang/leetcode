class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        scanned = [True] * (max(n+1, 2))
        scanned[0] = scanned[1] = False
        for i in range(2, n+1):
            if scanned[i]:
                for j in range(i*i, n+1, i):
                    scanned[j] = False
        return scanned.count(True)

if __name__ == '__main__':
    print Solution().countPrimes(10)