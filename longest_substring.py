# longest_substring.py
# Find the longest substring without repeating characters in a given string.


def longest_unique_substring(s):
    start = 0
    seen = {}
    max_sub = ""

    for i, ch in enumerate(s):
        if ch in seen and seen[ch] >= start:
            start = seen[ch] + 1
        seen[ch] = i
        current = s[start:i + 1]
        if len(current) > len(max_sub):
            max_sub = current
    return max_sub


if __name__ == "__main__":
    text = input("Enter a string: ")
    result = longest_unique_substring(text)
    print(f"Longest substring without repeating characters: {result}")
