

def shuffle_arr(nums, n):
    xnums = nums[:n]
    ynums = nums[n:]
    ans = []


    for i,j in zip(xnums, ynums):
        ans.extend([i,j])
    
    return ans




nums = [2,5,1,3,4,7]
n = 3
res = shuffle_arr(nums, n)
print(res)