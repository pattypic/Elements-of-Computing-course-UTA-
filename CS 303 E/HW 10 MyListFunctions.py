# File: MyListFunctions.py
# Student: Patrick Pichardo
# UT EID: pjp953
# Course: CS303E
#
# Date: 03/19/2023
# Description of Program:
# Each function hase its own description. Though on parts I got lazy. but everything works {:
# List funciton limitations:
#   indexing (but not slicing)
#   append (i.e., ``+'')
#   len, in, not in
#   equality comparison (== or !=))


lst1 = ["a", "b", "c"]
lst2 = [1, 2, 3, 4]
lst3 = [1, 2, 3, 1, 2, 3, 1, 2]

def myAppend( lst, x ): # Return a new list that is like lst but with the element x at the right end.
    return lst + [x] 

def myExtend( lst1, lst2 ): # Return a new list that contains the elements of lst1 followed by the elements of lst2 in order.
    return lst1 + lst2

def myMax( lst ):
    if len(lst) == 0:                         # Return the element with the highest value.
        print ("Empty list: no max value")    # If lst is empty, print "Empty list: no max value"
        return None                           # # and return None.  You can assume that the list
    else:                                     # elements can be compared.
        return max(lst)

def mySum( lst ): # Return the sum of the elements in lst. Assume that the elements are number.
    return sum(lst)

def myCount( lst, x ): # Return the number of times element x appear in lst.
    return lst.count(x)
    

def myInsert( lst, i, x ):      # Return a new list like lst except that x has been   
    new_lst = [] 
    if i < 0 or i > len(lst):   # inserted at the ith position.  I.e., the list is now
        print ("Invalid index") # one element longer than before. Print "Invalid index" if
        return None             # i is negative or is greater than the length of lst and 
    else:                       # return None.
        new_lst = lst.copy()
        new_lst.insert(i, x)
        return new_lst

def myPop( lst, i ):            # Return two results: 
    new_lst = []
    x = lst.copy()
    if i < 0 or i >= len(x):   # 1. the value that was removed.
        print ("Invalid index") # Print "Invalid index" if i is negative or is greater than
        return x, None        # or equal to len(lst), and return lst unchanged, and None
    else:                       # 2. a new list that is like lst but with the ith 
        new_lst = x.copy()    # element removed.
        removeval = new_lst.pop(i)        
        return new_lst, removeval

def myFind( lst, x ):
    for i in range(len(lst)):
        if lst[i] == x:
            return i         # Return the index of the first (leftmost) occurrence of 
    return -1                # x in lst, if any.  Return -1 if x does not occur in lst.

def myRFind( lst, x ):
    for i in range(len(lst)-1,-1,-1):
        if lst[i] == x:
            return i         # Return the index of the last (rightmost) occurrence of
    return -1                # x in lst, if any.  Return -1 if x does not occur in lst.

def myFindAll( lst, x ):
    new_lst = []
    for i in range(len(lst)):   # Return a list of indices of occurrences of x in lst, if any.
        if x == None:         # Return the empty list if there are none.
            return new_lst
        elif lst[i] == x:
            new_lst.append(i)
    return new_lst

def myReverse( lst ):
    new_lst = lst.copy()
    for i in range(len(lst) // 2):  # Return a new list like lst but with the characters
        x = new_lst[i]
        new_lst[i] = new_lst[len(lst) - i - 1]
        new_lst[len(lst) - i - 1] = x
    return new_lst

def myRemove( lst, x ):         
    new_lst = []                            # create an empty list to store the new elements
    removeV = None                          # create a variable to store the index of the first occurrence of x
    for i in range(len(lst)):               # loop over the elements in the input list         
        if lst[i] == x and removeV is None: # if we find the first occurrence of x, store its index                   
            removeV = i                     
        else:# if we haven't found the first occurrence of x yet or we've already found it, add the current element to the new list           
            new_lst.append(lst[i])          
    return new_lst                          # return the new list with x removed
                                     
def myRemoveAll( lst, x ):
    new_lst = []
    for i in range(len(lst)):
        if x == None:         
            return lst                  # If there are none, return lst.
        else:
            if lst[i] != x:
                new_lst.append(lst[i])
    return new_lst                      # Return a new list with all occurrences of x removed.

def mySlice( lst, i, j ):
    # A limited version of the slice operations on lists.
    # If i and j are in [0..len(lst)], return the list 
    # [ lst[i], lst[i+1], ... lst[j-1] ].  I.e., 
    # the slice lst[i:j].  Print an error message if either
    # i or j is not in [0..len(lst)].  Notice that this is 
    # similar but not identical to the way Python slice behaves.
    if i < 0 or j > len(lst): 
        return "Illegal index value"
    new_lst = []
    for k in range(i, j):
        new_lst.append(lst[k])
    return new_lst
    

print(myAppend( lst1, "d" ))        # Worked
print(myExtend( lst1, lst2 ))       # Worked
print(myExtend( lst2, lst1 ))       # Worked
print(myMax( lst1 ))                # Worked
print(myMax( lst2 ))                # Worked
print(mySum( lst2 ))                # Worked
print(myCount( lst1, "e" ))         # Worked
print(myCount( lst1, "a" ))         # Worked
print(myCount( lst3, 3))            # Worked
print(myInsert( lst1, 0, "d" ))     # Worked
print(myInsert( lst1, 2, "e" ))     # Worked
print(myInsert( lst1, 7, "e" ))     # Worked
print(myPop( lst1, 0 ))             # Worked
print(myPop( lst1, 2 ))             # Worked
print(myPop( lst1, 3 ))             # Worked
print(myFind( lst2, 1 ))            # Worked
print(myFind( lst2, 3 ))            # Worked
print(myFind( lst2, 5 ))            # Worked
print(myRFind( lst3, 3 ))           # Worked
print(myRFind( lst3, 1 ))           # Worked
print(myRFind( lst3, 4 ))           # Worked
print(myFindAll( lst3, 1 ))         # Worked
print(myFindAll( lst3, 4 ))         # Worked
print(myReverse( lst2 ))            # Worked
print(myReverse( lst3 ))            # Worked
print(myReverse( [1, "a", 2.5] ))   # Worked
print(myRemove( lst3, 1 ))          # Worked
print(myRemove( lst3, 3 ))          # Worked
print(myRemoveAll( lst3, 1 ))       # Worked
print(myRemoveAll( lst3, 5 ))       # Worked
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(mySlice( lst, 0, 5 ))         # Worked
print(mySlice( lst, 2, 8 ))         # Worked
print(mySlice( lst, -2, 8 ))        # Worked
print(mySlice( lst, 0, 11 ))        # Worked
print(mySlice( lst, 0, 12 ))        # Worked
print(mySlice( lst, 4, 1 ))         # Worked
print(mySlice( lst, 3, 3 ))         # Worked
# Nice
