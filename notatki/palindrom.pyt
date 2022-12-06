def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = (input("podaj slowo jakie chcesz sprawdzic "))
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")