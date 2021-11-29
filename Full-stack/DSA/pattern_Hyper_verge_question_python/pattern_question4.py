# n = 4
# 11112
# 32222
# 33334
# 54444

n=int(input("enter a ny number---"))
for i in range(1,n+1):
    if i%2==0:
       print(str(i+1)+n*str(i))
    else:
        print(n*str(i)+str(i+1))
        