# write a program to cope the content of one file to another file

def copy_file_content(source_file, destination_file):
    try:
        with open (source_file, "r") as src:
            content = src.read()
        with open(destination_file, "w") as dst:
            dst.write(content)
        print(f"Content copied from {source_file} to {destination_file}.")
    except FileNotFoundError:
        print(f"Error: The file '{source_file}' does not exist.")

# Example usage
copy_file_content("data.txt", "copied_data.txt")        

