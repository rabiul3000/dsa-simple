
strs = [1,2,3,4,5]
start = strs[0]
n = len(strs)
# prefix = strs[0]
# n = len(strs)

# for i in range(1, n):
#     while not strs[i].startswith(prefix):
#         prefix = prefix[:-1]

# print(prefix)

for i in range(1, n):
    if strs[i] != strs[start]:
        start = start+1
        strs[start] = strs[i]
print (start + 1)

        