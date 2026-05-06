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










