# Create a program that counts the number of occurences of a specific word in a file
def count_word_occurrences(file_path, word):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            word_count = content.lower().split().count(word.lower())
        print(content)
        print(f"The word '{word}' occurs {word_count} times in the file '{file_path}'.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")

# Example usage
count_word_occurrences("data.txt", "And")