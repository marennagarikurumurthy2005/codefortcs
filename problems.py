#finding the second largest number using python  in an arr

raw="10,65,7,9,63,90"
opt=list(map(int,raw.split(",")))
largest=opt[0]
second_largest=0
for i in opt:
    if i>largest:
        second_largest=largest
        largest=i
    if i> second_largest and i!=largest:
        second_largest=i
print(second_largest)

    


