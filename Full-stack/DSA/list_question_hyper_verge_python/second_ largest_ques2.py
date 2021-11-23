# Find second largest/ second smallest element in an array
#  ( expected time complexity: O(n), single traversal )

# numbers=[ -40, -23, -2, -5, -1]


# second largest...

numbers=[10,20,40,50,30,90]
i=0
index=0
second=numbers[0]
store=numbers[0]
while index<len(numbers):
    if numbers[index]>store:
        store=numbers[index]
    else:
        second=numbers[index]
    index=index+1
while i<len(numbers):
    if second<numbers[i]<store:
        second=numbers[i]
    i=i+1
print("second largest number",second)
