class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        result = [-1] * 2
    	
        # find the right bound
        l, r = 0, len(A) - 1
        while l + 1 < r:
        	m = (l + r) >> 1
        	if target >= A[m]:
        		l = m
        	else:
        		r = m
        if A[r] == target:
        	result[1] = r
        elif A[l] == target:
        	result[1] = l
        else:
        	return result
        		
        # find the left bound
        l, r = 0, result[1]
        while l + 1 < r:
        	m = (l + r) >> 1
        	if target > A[m]:
        		l = m
        	else:
        		r = m
        result[0] = (l if A[l] == target else r)
        	
        return result
