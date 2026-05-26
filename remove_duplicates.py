# remove_duplicates.py
# Remove duplicate elements from a list without using built-in deduplication functions.


def remove_duplicates(items):
    unique_items = []
    for item in items:
        found = False
        for unique in unique_items:
            if item == unique:
                found = True
                break
        if not found:
            unique_items.append(item)
    return unique_items


if __name__ == "__main__":
    raw = input("Enter comma-separated values: ")
    values = [value.strip() for value in raw.split(",")]
    result = remove_duplicates(values)
    print(f"After removing duplicates: {result}")
