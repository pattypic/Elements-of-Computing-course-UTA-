# File: RecursiveFunctions.py
# Student: Patrick Pichardo
# UT EID: pjp953
# Course: CS303E
#
# Date: 04/07/2023
def sumItemsInList( L ):
    """ Given a list of numbers, return the sum. """
    if L == []:
       return 0
    else:
       return L[0] + sumItemsInList( L[1:] )

def countOccurrencesInList( key, L ):
    """ Return the number of times key occurs in list L. """
    if not L:                 # same as L == []:
       return 0
    elif key == L[0]:
       return 1 + countOccurrencesInList( key, L[1:] )
    else:
       return countOccurrencesInList( key, L[1:] )

def addToN ( n ):
   """ Return the sum of the non-negative integers to n.
   E.g., addToN( 5 ) = 0 + 1 + 2 + 3 + 4 + 5. """
   if n == 0:
      return 0
   else:
      return n + addToN( n - 1 )

def findSumOfDigits( n ):
   """ Return the sum of the digits in a non-negative integer. """
   if n == 0:
      return 0
   else:
      return n % 10 + findSumOfDigits(n // 10)

def integerToBinary( n ):
   """ Given a nonnegative integer n, return the 
   binary representation as a string. """
   if n == 0:
      return '0'
   else:
        binary = integerToBinary(n // 2) + str(n % 2)
        return binary.lstrip('0')

def integerToList( n ):
   """ Given a nonnegative integer, return a list of the 
   digits (as strings). """
   if n == 0:
      return [0]
   else:
      return integerToList(n // 10) + [str(n % 10)]

def isPalindrome( s ):
   """ Return True if string s is a palindrome and False
   otherwise. Count the empty string as a palindrome. """
   if len(s) <= 1:
      return True
   elif s[0] == s[-1]:
      return isPalindrome( s[1:-1] )
   else:
      return False

def findFirstUppercase( s ):
   """ Return the first uppercase letter in 
   string s, if any. Return None if there
   is none. """
   if not s:
      return None
   elif s[0].isupper():
      return s[0]
   else:
      return findFirstUppercase( s[1:] )

# for this one, don't reverse the string.
def findLastUppercase( s ):
   """ Return the last uppercase letter in 
   string s, if any. Return None if there
   is none. """
   if not s:
      return None
   elif s[-1].isupper():
      return s[-1]
   else:
      return findLastUppercase( s[:-1] )

def findFirstUppercaseIndexHelper( s, index ):
   """ Helper function for findFirstUppercaseIndex.
   Return the index of the first uppercase letter;
   assume you are starting at index. Return -1 
   if there is none."""
   if index >= len(s):
      return -1
   elif s[index].isupper():
      return index
   else:
      return findFirstUppercaseIndexHelper( s, index + 1 )


# The following function is already completed for you. But 
# make sure you understand what it's doing. 

def findFirstUppercaseIndex( s ):
   """ Return the index of the first uppercase letter in 
   string s, if any. Return -1 if there is none. This one 
   requires a helper function, which is the recursive 
   function. """
   return findFirstUppercaseIndexHelper( s, 0 )

# sumItemsInList.__doc__  IDK if it worked                      # shows using docstring
' Given a list of numbers, return the sum. '
# countOccurrencesInList.__doc__ IDK if it worked
' Return the number of times key occurs in list L. '
print(addToN( 10 ))
# 55 yup
print(addToN( 100 ))
# 5050 uhuh
print(addToN( 0 ))
# 0  yessir
print(findSumOfDigits( 0 ))
# 0     yup
print(findSumOfDigits( 12345 ))
# 15    right
print(integerToBinary( 25 ))
# '11001'   yup
print(integerToBinary( 100 ))
# '1100100' uhhuh
print(integerToBinary( 0 ))
# '0'   yessir
print(integerToList( 123 ))
# ['1', '2', '3']  okayyy
print(integerToList( 348914 ))
# ['3', '4', '8', '9', '1', '4']  first try
print(integerToList( 0 ))
# ['0']    second try                    # this function is easier if you return
                                 # this for 0
print(isPalindrome( "abcDcba" ))
# True      yup
print(isPalindrome( "abcDcbaF" ))
# False     got it
print(isPalindrome( "" ))
# True      slay
print(isPalindrome( "X" ))
# True      slaying more
print(findFirstUppercase( "ab c  dEFg hi" ))
# 'E' got it
print(findFirstUppercase( "ab c  defg hi" ))       # None doesn't print in interactive mode
# None did print
print(findLastUppercase("ABcdE Fghi"))
# 'F'  yup
print(findLastUppercase(""))
print(findLastUppercase("abcdefghi"))
print(findFirstUppercaseIndexHelper("abCd", 7))
# 9 
print(findFirstUppercaseIndexHelper("abCd", 10))
# 12 
print(findFirstUppercaseIndexHelper("abcd", 10))
# -1 i mean i got it but 
print(findFirstUppercaseIndexHelper("abCd", 0))
# 2   check
print(findFirstUppercaseIndex("abCd"))
# 2   check
print(findFirstUppercaseIndex( "ab c  dEFg hi" ))
# 7   check
print(findFirstUppercaseIndex( "ab c  defg hi" ))
# -1   check
print(findFirstUppercaseIndex( "" ))
# -1   check