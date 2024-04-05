import re
import os

input_file_prefix = 'page_'

# Get a list of input files
input_files = [filename for filename in os.listdir('.') if filename.startswith(input_file_prefix)]

for input_file in input_files:
    # Extract the page number from the input file name
    page_number = input_file[len(input_file_prefix):-4]  # Remove prefix and ".txt" extension

    domains = set()

    # Read lines from input file with 'utf-8' encoding
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Process lines
    filtered_lines = []
    skip_line = False
    for line in lines:
        line = line.strip()

        # Skip lines containing "robots.txt"
        if line.endswith("robots.txt"):
            skip_line = True
            continue

        # Skip lines until a line starting with "http://" is found after "robots.txt"
        if skip_line and line.startswith("http://"):
            skip_line = False

        if not skip_line:
            # Extract domain name from URL
            match = re.search('(https?://[^/]+)', line)
            if match:
                domain = match.group(1)
                domains.add(domain)

    # Overwrite the input file with unique domain names
    with open(input_file, 'w', encoding='utf-8') as f:
        for domain in domains:
            f.write(domain + '\n')
