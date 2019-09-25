a=0
def reverse(s):
    return s[::-1]
def isPalindrome(s):
    rev = reverse(s)
    if (s == rev):
        return True
    return False
a = input("Enter the word   ")
s = str(a)
ans = isPalindrome(s)
if ans == 1:
    print(a ,"This is a palindrome")
else:
    print(a ,"This is not a palindrome")
