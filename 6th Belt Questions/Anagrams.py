str1, str2 = input().split()

if len(str1) != len(str2):
    print("Not Anagrams")
else:

    count1 = [0] * 26  
    count2 = [0] * 26  
    

    for i in range(len(str1)):
        count1[ord(str1[i]) - ord('a')] += 1
        count2[ord(str2[i]) - ord('a')] += 1
    
    is_anagram = True
    for i in range(26):
        if count1[i] != count2[i]:
            is_anagram = False
            break
    
    if is_anagram:
        print("Anagrams")
    else:
        print("Not Anagrams")
