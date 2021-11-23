# 1 2 3 4 5
# 11 12 13 14 15
# 21 22 23 24 25
# 16 17 18 19 20
# 6 7 8 9 10
# n = 5
n=5
empty1=[]
for i in range(1,n+1):
    empty2=[]
    for j in range(1,n+1):
        if i%2==0:
            empty2.append((i-1)*5 + j)
            # print(b)
        elif i == 1:
            print(j,end=' ')
        else:
            print((i-1)*5 + j,end=' ')
    if i%2==0:
        print()
    empty1.append(empty2)
    # print(a)
# print()
for i in range(len(empty1),0,-1):
        for j in empty1[i-1]:
            print(j,end=' ')
        print()

# We have taken Empty 1 list because we save you 2 list in it:
# First [6,7,8,9,10] and second [16,17,18,19,20] and the rest we list directly.
# Print Res :... Then run in reverse from the last loop we took so that both of them.
# We print the list in a nested for loop: