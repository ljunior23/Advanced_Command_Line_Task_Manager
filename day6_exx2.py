def write_item_to_file(filename, items):
    with open(filename, "w") as file:
        for item in items:
            file.write(item + "\n")
   
        
def read_items_from_file(filename):
    try:
        with open(filename, "r") as file:
            data = file.readlines()
            print("Items in the file:")
            for line in data:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        
write_item_to_file("data2.txt", ["Hello", "I'm now learning to become", "an AI engineer so God help me", "and also make my union with Genie possible Amen"])
read_items_from_file("data3.txt")