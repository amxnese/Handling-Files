def count_word_occurrences(file_path, target_word):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content.split())
            word_count = content.lower().split().count(target_word.lower())
            print(f"The word '{target_word}' appears {word_count} times in the file.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = input("Enter File Path: ")
target_word = input("Enter the word to count: ")
count_word_occurrences(file_path, target_word)
