#arrays
#Strings
#dictonaries
#sorting
#trees
#graphs
#stack
#queues
#searching
#linked-list



#finding the second largest number using python  in an arr

# raw="10,65,7,9,63,90"
# opt=list(map(int,raw.split(",")))
# largest=opt[0]
# second_largest=0
# for i in opt:
#     if i>largest:
#         second_largest=largest
#         largest=i
#     if i> second_largest and i!=largest:
#         second_largest=i
# print(second_largest)


# checking prime number or not 

# given="""[10,"20",5]"""

# data=list(map(int,given.strip("[]").replace('"','').split(",")))

# print(*data)
# for i in data:
#     flag=1
#     for j in range(2,i):
#         if i%j==0:
#             flag=0
#             break
#     if flag:
#         print(i," is prime")

# reversing a number

# given=int(input("Enter a number:"))
# res=0
# while given>0:
#     rem=given%10
#     given//=10
#     res=rem+res*10
# print(res)

# armstrong number 
# num=10
# l=len(str(num))
# tar=0
# while num>0:
#     rem=num%10
#     num//=10
#     tar=tar+rem**l
# print(tar)


# fibonacci number of sequence 10
# a,b=0,1
# n=10
# for i in range(n):
#     print(a)
#     c=a+b
#     a=b
#     b=c


# remove duplicates in given list 

# raw="10,15,8,6,8,10"
# data=list(map(int,raw.split(",")))
# print(data)
# new_data=set(data)
# print(new_data)
# samp=[]
# for i in data:
#     if i not in samp:
#         samp.append(i)
# print(samp)

# anagrams




# data=["cat","tac","act","mac","cam","ban","van"]
# res=[]
# count=0
# while count<len(data):
#     dumb=[]
#     an1={}
#     for i in data[count]:
#         if i in an1:
#             an1[i]+=1
#         else:
#             an1[i]=1
#     for j in data:
#         an2={}
#         if j!=data[count]:
#             for k in j:
#                 if k in an2:
#                     an2[k]+=1
#                 else:
#                     an2[k]=1
#         if an1==an2:
#             if data[count] in dumb:
#                 dumb.append(j)
#             else:
#                 dumb.append(data[count])
#                 dumb.append(j)
#     res.append(dumb)
#     count+=1
    
# print(res)


# data=["list","tuple","mk","var","car"]
# for i in range(len(data)):
#     for j in range(i+1,len(data)):
#         if len(data[i])>len(data[j]):
#             data[i],data[j]=data[j],data[i]
# print(data)

# arr=[10,0,20,90,40,0,50,10]
# for i in arr:
#     print(arr.count(i))
# ar1=[]
# ar2=[]
# for i in arr:
#     if i==0:
#         ar1.append(i)
#     else:
#         ar2.append(i)
# print(ar2+ar1)
# for i in range(len(arr)):
#     # for j in range(i+1,len(arr)):
#     #     if arr[i]<arr[j]:
#     #         arr[i],arr[j]=arr[j],arr[i]
    

# print(arr)

# n=int(input("Enter number of operations"))
# data=[]
# for i in range(n):
#     d=input().split("")
#     data.append(d)
# print(data)
















