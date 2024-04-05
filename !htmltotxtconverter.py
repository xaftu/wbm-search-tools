import os

# Get the current directory
current_dir = os.getcwd()

# Get a list of all files in the current directory
files = os.listdir(current_dir)

# Iterate over each file
for file in files:
    # Check if the file is an HTML file
    if file.endswith(".html"):
        # Create a new file name with the TXT extension
        new_file = os.path.splitext(file)[0] + ".txt"

        # Rename the file
        os.rename(file, new_file)

        print(f"Renamed {file} to {new_file}")

print("Conversion complete.")
