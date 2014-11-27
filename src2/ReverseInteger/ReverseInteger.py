class Solution:
    # @return an integer
    def reverse(self, x):
    	strX = str(x)
    	#strX = list(strX)
    	prefix = ''
    	if strX[0] == '-':
    		strX = strX[1:]
    		prefix = '-'

    	strX = list(strX)
    	strX.reverse()
    	strX = prefix + ''.join(strX)
    	x = int(strX)
    	if x > 2147483647:
    		return 0
    	if x < -2147483648:
    		return 0
    	return x
     

if __name__ == '__main__':
	print Solution().reverse(2147483647)
	print Solution().reverse(0)