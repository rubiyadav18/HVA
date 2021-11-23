# 1 2 3 4
# 9 10 11 12
# 13 14 15 16
# 5 6 7 8
# n = 4


n=4
empty_list=[]
# Here I have taken a empty  list
# because  i have to store the last no
# like 5,6,7,8,

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==2:
            empty_list.append(j+4)
        elif i==1:
            print(j,end=' ')
        else:
             print((i-1)*4+j,end=' ')
    if j!=2:
        print()
for i in empty_list:
         print(i,end=' ')


# See, we store the number in a
#  list: and we append that list to the empty:
# Nested list
         


