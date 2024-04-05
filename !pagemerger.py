import os

input_file_prefix = 'page_'
merged_file_prefix = 'merged_cdx_'
lines_per_file = 100000

# Get a list of input files
input_files = [filename for filename in os.listdir('.') if filename.startswith(input_file_prefix)]

lines_count = 0
file_count_start = 50  # Enter the starting number for merged_cdx files
file_count = file_count_start
merged_file = merged_file_prefix + str(file_count) + '.txt'

with open(merged_file, 'w', encoding='utf-8', errors='ignore') as f_out:
    for input_file in input_files:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as f_in:
            for line in f_in:
                f_out.write(line)
                lines_count += 1

                # Create a new merged file if the line limit is reached
                if lines_count == lines_per_file:
                    lines_count = 0
                    file_count += 1
                    merged_file = merged_file_prefix + str(file_count) + '.txt'
                    f_out.close()  # Close the current file
                    f_out = open(merged_file, 'w', encoding='utf-8', errors='ignore')  # Open a new file for writing

        # Delete the input file after merging
        os.remove(input_file)