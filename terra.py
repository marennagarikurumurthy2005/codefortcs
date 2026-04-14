# distance of nearest fib to sum of arr
# arr=[2,4,6,8,15,6,90]
# total_arr_sum=sum(arr)
# a,b=0,1
# while b<total_arr_sum:
#     c=a+b
#     a=b
#     b=c

# dist=0
# print(a,total_arr_sum,b)
# if total_arr_sum-a<b-total_arr_sum:
#     dist=total_arr_sum-a

# else:
#     dist=b-total_arr_sum
# print(dist)


# # print(total_arr_sum)
# min_fib=0
# max_fib=0
# a,b=0,1
# while min_fib<total_arr_sum:
#     c=a+b
#     a=b
#     b=c
#     min_fib=c

# max_fib=min_fib+a+b

# min_diff=0
# if max_fib-total_arr_sum<total_arr_sum-min_fib:
#     min_diff=max_fib-total_arr_sum
# else:
#     min_diff=total_arr_sum-min_fib

# print(min_diff)




# time calculation 10:30am to 10:30pm

# def cal(p):
#     time,period=p[:-2],p[-2:]
#     h,m=time.split(":")
#     h=int(h)
#     m=int(m)

#     if period=="am":
#         if h==12:
#             h=0
#     else:
#         if h!=12:
#                 h+=12
#     return h*60+m

# inpu="10:10pm-10:11am"
# start,end=inpu.split("-")
# st=cal(start)
# et=cal(end)


# if et<st:
#      res = (1440 - st) + et
# else:
#     res=et-st
# print(res)
# print(res//60,res%60)

# print(start)
# print(end)
# p=start
# time,period=p[:-2],p[-2:]
# print(time)
# print(period)

# add * for odd and - for even 


# arr="0245769246975"
# newarr=""
# for i in range(len(arr)-1):
    
#     if int(arr[i])%2==0 and int(arr[i+1])%2==0 and int(arr[i])!=0:
#         newarr=newarr+arr[i]+"*"
#     elif int(arr[i])%2!=0 and int(arr[i+1])%2!=0:
#         newarr=newarr+arr[i]+"-"
#     else:
#         newarr=newarr+arr[i]
# newarr=newarr+arr[-1]


# print(newarr)

# check arr follows arithmetic or geometric or else return -1

# arr=[2,4,8,16]
# ap=True
# apdif=arr[1]-arr[0]
# for i in range(len(arr)-1):
#     #  print(arr[i+1],arr[i])
#      if arr[i+1]-arr[i]!=apdif:
#           ap=False
#           break
# # print(ap)

# gp=False
# if ap==False and arr[0]!=0:
#      gp=True
#      gprat=arr[1]/arr[0]
#      for i in range(len(arr)-1):
#           if arr[i+1]/arr[i]!=gprat:
#                gp=False
#                break
# if ap:
#      print("ap")
# elif gp:
#      print("gp")
# else:
#      print("-1")



# time conversion


# def cal(data):
#     time,period=data[:-2],data[-2:]
#     h,m=time.split(":")
#     h=int(h)
#     m=int(m)
#     if period=="am":
#         if h==12:
#             h=0
#     else:
#         if h!=12:
#             h+=12
#     return h*60+m   #610=600   10
    
# string="10:10am-12:20am"    # 10 -> 12 ->00:10

# start,end=string.split("-")
# # print(start)
# # print(end)

# st=cal(start)
# et=cal(end)

# if et<st:
#     res=(1440-st)+et
# else:
#     res=et-st
# print(res)

# print(res//60,":",res%60)




















