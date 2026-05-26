# anagram.py
# Check whether two strings are anagrams of each other.
# Anagrams are words or phrases formed by rearranging the letters of another.


def normalize(text):
    return sorted(text.replace(" ", "").lower())


def is_anagram(str1, str2):
    return normalize(str1) == normalize(str2)


if __name__ == "__main__":
    first = input("Enter the first text: ")
    second = input("Enter the second text: ")
    if is_anagram(first, second):
        print("The texts are anagrams.")
    else:
        print("The texts are not anagrams.")
