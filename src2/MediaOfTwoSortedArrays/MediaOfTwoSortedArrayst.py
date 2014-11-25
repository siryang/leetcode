'''
There are two sorted arrays A and B of size m and n respectively. 

Find the median of the two sorted arrays. 

The overall run time complexity should be O(log (m+n)).
'''

class Solution:
    # get media of A --> ma
    # get count of number in B that smaller than ma
    def getNumBiggerThanValue(self, Array, Value):
        # lower bounder is better
        for i in range(len(Array)):
            if Array[i] > Value:
                return i + 1
        return len(Array)

    # return iA, iB
    def moveFoward(self, A, B, iA, iB):
        # min of A[iA + 1], B[iB]
        if iB == len(B):
            return iA + 1, iB
        elif iA == len(A):
            return iB + 1, iA
        else

    # @return a float
    def findMedianSortedArrays(self, A, B):
        lenA = len(A)
        lenB = len(B)
        mid = (lenA + lenB) / 2
        if lenA >= lenB:
            iA = len(A) / 2
            iB = self.getNumBiggerThanValue(B, A[iA])
        else:
            iB = len(B) / 2
            iA = self.getNumBiggerThanValue(A, B[iB])
        A.append(0x8ffffffff)
        B.append(0x8ffffffff)

        while True:
            ## step
            left = iA + iB
            #print mid, left, iA, iB, ".."
            if left == mid:
                return min(A[iA], B[iB])
            elif left < mid:
                # step forward
                if A[iA - 1] > B[iB - 1]:
                    iB+=1
                else:
                    iA+=1
            elif left > mid:
                # step backward
                if A[iA] > B[iB]:
                    iA-=1
                else:
                    iB-=1
            #print "A:%d, B:%d" %(A[iA], B[iB])
            

if __name__ == '__main__':
    slu = Solution()
    print slu.findMedianSortedArrays([1], [2])
    print slu.findMedianSortedArrays([1, 12, 15, 26, 38], [2, 13, 17, 30, 45, 50])
    print slu.findMedianSortedArrays([1, 12, 15, 26, 38], [2, 13, 17, 30, 45])
    print slu.findMedianSortedArrays([1, 2, 5, 6, 8], [13, 17, 30, 45, 50])
    print slu.findMedianSortedArrays([1, 2, 5, 6, 8, 9, 10], [13, 17, 30, 45, 50])
    print slu.findMedianSortedArrays([1, 2, 5, 6, 8, 9], [13, 17, 30, 45, 50])
    print slu.findMedianSortedArrays([1, 2, 5, 6, 8], [11, 13, 17, 30, 45, 50])
    print slu.findMedianSortedArrays([1], [2,3,4])
    ## [1,2,3] --> 2
    ## [1,2,3,4] --> 3
    ## [1,2,4,5,5,8] ==> 5
    ## [1,2,4,5,5,6,8] ==> 5
        


            
