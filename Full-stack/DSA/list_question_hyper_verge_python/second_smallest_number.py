# second_smallet number

numbers=[10,6,15,25,30,20,10,40]
i=0
index=0
second=numbers[0]
store=numbers[0]
while index<len(numbers):
    if numbers[index]<store:
        store=numbers[index]
    else:
        second=numbers[index]
    index=index+1
    
while i<len(numbers):
    if second>numbers[i]>store:
        second=numbers[i]
    i=i+1
print("second smallest number",second)