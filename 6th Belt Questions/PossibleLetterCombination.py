a = input()
b = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

arr1 = [""]
    
for i in a:
    char = b[i]
    arr2 = []
    for j in arr1:
        for k in char:
            arr2.append(j + k)
    arr1 = arr2
    arr1.sort()
print(*arr1)
