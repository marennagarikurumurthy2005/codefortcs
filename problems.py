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

given=int(input("Enter a number:"))
res=0
while given>0:
    rem=given%10
    given//=10
    res=rem+res*10
print(res)







