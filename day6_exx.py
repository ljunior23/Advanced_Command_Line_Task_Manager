# Exx 1: count words and lines in a file

def count_words_and_lines(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.readlines()
            line_count = len(content)
            word_count = sum(len(words.split()) for words in content)
        print(f"Word Count: {word_count}")
        print(f"Line Count: {line_count}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    
count_words_and_lines("data.txt")
    