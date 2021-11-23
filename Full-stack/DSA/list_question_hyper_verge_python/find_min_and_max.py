# Finding Max  in a single Scan..
list1=[1,2,45,4,5,6,9,100]
max=0
i=0
while i<len(list1):
    if list1[i]>max:
        max=list1[i]
    i+=1
print(max)


