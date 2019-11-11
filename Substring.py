# Given two strings 'X' and 'Y', find the length of the longest common substring.

def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if len(match) > len(answer): answer = match
                match = ""
    return answer


print(longestSubstringFinder("pumpkin pie available", "pumpkin pies"))
print(longestSubstringFinder("apples", "appleses"))
print(longestSubstringFinder("bapples", "cappleses"))
print(longestSubstringFinder("appleeeeeees", "eeeeeecherrio"))

# string1 = "apple"
# string2 = "banana" + string1[1]
# print(string2)
