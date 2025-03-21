def is_palindrome(s):
    return s == s[::-1]
string = "radar"
print(f"Is'{string}'a palindrome? {is_palindrome(string)}.")

