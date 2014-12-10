'''

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a <= b <= c <= d)
The solution set must not contain duplicate quadruplets.

 For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
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
	# @return a list of lists of length 4, [[val1,val2,val3,val4]]
	def fourSum(self, num, target):
		mapping = []
		num.sort()
		itemNum = len(num)
		for s in range(0, itemNum - 3):
			if s != 0 and num[s] == num[s-1]:
				continue

			for e in reversed(range(s + 3, itemNum)):
				if e != itemNum-1 and num[e] == num[e+1]:
					continue

				sumSE = num[s] + num[e]
				neededBySE = target - sumSE

				if neededBySE < num[s+1]*2 or num[e-1]*2 < neededBySE:
					continue

				for s2 in range(s + 1, e - 1):
					if s2 != s+1 and num[s2] == num[s2-1]:
						continue

					needed = neededBySE - num[s2]
					if needed < num[s2 + 1]:
						continue
					if not binary_search(num[s2+1:e], needed) is None:
						mapping.append([num[s], num[s2], needed, num[e]])
		return mapping

if __name__ == '__main__':
	#print Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
	#print Solution().fourSum([0,0], 0)
	print Solution().fourSum([-1,2,2,-5,0,-1,4], 3)


