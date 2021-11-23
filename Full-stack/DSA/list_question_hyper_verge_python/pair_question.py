# Finding a Pair of Elements with sum K in Sorted Array
list1=[2,4,8,7,6,10]
i=0
pair=11
empty=[]
while i<len(list1):
    j=0

    while j<len(list1):
        if list1[i]+list1[j]==pair:
            empty.append(list1[i])
            empty.append(list1[j])
        j+=1
    i+=1
print(empty)

