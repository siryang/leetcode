'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, 

where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
    	match = dict()

    	for i in range(len(num)):
    		v = match.get(num[i], None)
    		if v != None:
    			return v + 1, i + 1

    		match[target - num[i]] = i

    	return None

if __name__ == '__main__':
	s = Solution();
	print s.twoSum([3,2,4], 6)
        