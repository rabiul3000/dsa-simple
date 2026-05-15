""""
You are given an integer array nums. We consider an array good if it is a permutation of an array base[n].

base[n] = [1, 2, ..., n - 1, n, n] (in other words, it is an array of length n + 1 which contains 1 to n - 1 exactly once, plus two occurrences of n). For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].

Return true if the given array is good, otherwise return false.

Note: A permutation of integers represents an arrangement of these numbers.


"""


def isGood(nums):

    pointer = 0
    
    for i in range(1, len(nums)):
        if nums[pointer] > nums[i]:
            
            nums[i] = nums[pointer]
            
        pointer +=1
    return nums
    



nums = [3,2,1,3]
ans = isGood(nums)
print(ans)
