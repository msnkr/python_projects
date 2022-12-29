
# Get list of items as int.
# If list 1 already in list 2, don't copy items

with open('./Day 26/file1.txt')as f1:
    data1 = f1.read().splitlines()
    
with open('./Day 26/file2.txt')as f2:
    data2 = f2.read().splitlines()
    
result = [int(num) for num in data1 if num in data2]

# Write your code above 👆


print(result)


