# File: MyStringFunctions.py
# Student: Patrick Pichardo
# UT EID: pjp953
# Course: CS303E
#
# Date: 02/28/2023
# Description of Program: There is a comment on each def, in show this defines some funcitons
# {myAppend, myCount, myExtend, myMin, myInserts, myPop, myFind, myRFind, myRemove, myRemoveAll, myReverse}

s1 = "abcd"
s2 = "efgh"
x = "iubiubonkd"

# Append a character to a string
def myAppend(s, ch):
    s += ch
    return s

# Count the number of occurrences of a character in a string
def myCount(s, ch):
    cnt = s.count(ch)
    return cnt

# Concatenate two strings
def myExtend(s1, s2):
    return s1 + s2

# Find the minimum character in a string
def myMin( s ):
    if s == " ":
        print("Empty string: no min value")
        return None
    else:
        return min(s)

# Insert a character into a string at a specified position
def myInsert(s, i, ch):
    if i > len(s):
        print("Invalid index")
        return None
    else:
        return s[:i] + ch + s[i:]

# Remove and return a character at a specified position
def myPop( s, i ):
    if i > len(s):
        print("Invalid index")
        return None
    else:
        x = s[i]
        s = s[:i] + s[i+1:]
        return s, x

# Find the index of the first occurrence of a character in a string
def myFind( s, ch):
    for i in range(len(s)):
        if s[i] == ch:
            return i
    return -1

# Find the index of the last occurrence of a character in a string
def myRFind(s, ch):
    index = -1
    for i in range(len(s)):
        if s[i] == ch:
            index = i
    return index

# Remove the first occurrence of a character from a string
def myRemove( s, ch):
    if ch not in s:
        return s
    else:
        for i in range(len(s)):
            if s[i] == ch:
                return s[:i] + s[i + 1:]

# Remove all occurrences of a character from a string
def myRemoveAll(s, ch):
    if ch not in s:
        return s
    else:
        x = ""
        for c in s:
            if c != ch:
                x += c
        return x

# Reverse a string
def myReverse(s):
    if s == " ":
        return " "
    return s[::-1]

print(myAppend(s1, "e"))
print(myCount(s1, "a"))
print(myExtend(s1, s2))
print(myMin( x ))
print(myInsert(s1, 2, "d"))
print(myPop(s1, 2))
print(myFind("abcdabcd", "a"))
print(myRFind("duinfg", "g"))
print(myRemove("abcdabcd", "a"))
print(myRemoveAll("abcabcabca", "a"))
print(myReverse("hannah"))


