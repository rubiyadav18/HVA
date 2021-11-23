user=int(input("enter a any number----"))
list1=[1,2,3,4,5,6,7,17,45]
index=0
empty=[]
for i in range(len(list1)):
    if  user in list1:
        print("this number is in  arrya",user)
        break
    else:
        print('this  number is not in arrya', user)
        break