def main():
    """Run the main logic of the script."""
    mixed_list = [10, "apple", 3.14, "banana", True, "cherry", None, [1, 2], "penguin67", "penguin??"]

    string_count = 0
    
    for element in mixed_list:
        if type(element) is str:
            string_count += 1

    print(f"Number of string elements: {string_count}")

if __name__ == "__main__":
    main()
