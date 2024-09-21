n = int(input()) 
arr1 = [input() for _ in range(n)] 

# Initialize variables
max_len = 0
arr2 = [""]

# Iterate over each i in the array
for i in arr1:
    char = set(i)
    
    # Skip if the i has duplicate characters
    if len(char) != len(i):
        continue

    # Update arr2 by appending the current i
    arr3 = []
    for j in arr2:
        combined = j + i
        
        # Check if combined i has unique characters
        if len(set(combined)) == len(combined):
            arr3.append(combined)
            max_len = max(max_len, len(combined))
    
    arr2.extend(arr3)
print(max_len)
