
"""

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.


"""

def findMaxConsecutiveOnes(nums):
    counter = 0
    record = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            counter+=1
            record = max(counter, record)
        else:
            counter = 0
    return record
        
    






 
nums = [1,1,0,1,1,1]

ans = findMaxConsecutiveOnes(nums)
print(ans)