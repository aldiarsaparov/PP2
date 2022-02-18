def isPalindrome(s):
    return s == s[::-1]


if isPalindrome(input()):
    print("Yes")
else:
    print("No")
