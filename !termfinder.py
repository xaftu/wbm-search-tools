import os

# Get the current directory
current_directory = os.getcwd()

# Prompt user for search term
search_term = input("Enter search term: ")

# Get a list of all text files in the current directory
text_files = [file for file in os.listdir(current_directory) if file.endswith(".txt")]

# Create the file for storing lines containing the search term
terms_found_file = os.path.join(current_directory, "!termsfound.txt")

# Iterate through each text file and perform search
with open(terms_found_file, "w", encoding="utf-8") as outfile:
    for file_name in text_files:
        file_path = os.path.join(current_directory, file_name)

        # Open the file and read its contents
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        # Perform search and write matching lines to the terms found file
        for line in lines:
            if search_term in line:
                outfile.write(line)

print("Search completed. Results are stored in termsfound.txt.")