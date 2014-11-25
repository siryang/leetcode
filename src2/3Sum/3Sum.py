
'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)

The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)

'''
def binary_search(array, value):
	low, high = 0, len(array)
	while low < high:
		mid = (low + high) / 2
		midval = array[mid]
		if midval < value:
			low = mid+1
		elif midval > value:
			high = mid
		else:
			return mid

	return None

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]\
    def threeSum(self, num):
    	mapping = []
    	num.sort()
    	numLen = len(num)

    	# i step forward
    	for i in range(numLen):
    		if num[i] > 0 or (num[i] == num[i-1] and i != 0):
    			continue

			# j step backward
    		for j in range(i + 1, numLen):
    			j = numLen + i - j
    			if j + 1 != numLen and num[j] == num[j+1]:
    				continue

    			needed = 0-num[i]-num[j]
    			if needed < num[i]:
    				continue
    			if needed > num[j]:
    				break 
    				
    			# binary_search is better for find middle value
    			if binary_search(num[i+1:j], needed) != None: 
    				mapping.append([num[i], needed, num[j]])

        return mapping


if __name__ == '__main__':
	rst = Solution().threeSum([-2, -1, 0, 1, 2, 3])
	rst.sort()
	print rst
	print Solution().threeSum([])
