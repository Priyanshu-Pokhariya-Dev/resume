# palindrome.py
# Check whether a string is a palindrome.
# A palindrome reads the same backward and forward.


def is_palindrome(text):
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    value = input("Enter text to check for palindrome: ")
    if is_palindrome(value):
        print(f"\"{value}\" is a palindrome.")
    else:
        print(f"\"{value}\" is not a palindrome.")
