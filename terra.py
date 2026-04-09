# nearest fib to sum of arr

# time calculation 10:30am to 10:30pm

# add * for odd and - for even 


arr="0245769246975"
newarr=""
for i in range(len(arr)-1):
    
    if int(arr[i])%2==0 and int(arr[i+1])%2==0 and int(arr[i])!=0:
        newarr=newarr+arr[i]+"*"
    elif int(arr[i])%2!=0 and int(arr[i+1])%2!=0:
        newarr=newarr+arr[i]+"-"
    else:
        newarr=newarr+arr[i]
newarr=newarr+arr[-1]


print(newarr)

# check arr follows arithmetic or geometric or else return -1
