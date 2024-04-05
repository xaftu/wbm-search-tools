import requests
import time
from concurrent.futures import ThreadPoolExecutor

# Define the base URL pattern
base_url = "https://web.archive.org/cdx/search/cdx?url=*.example.com&fl=original&collapse=urlkey&page="
start_page = 0

# Number of pages to download
num_pages = 100

# Function to download a page
def download_page(page_number):
    url = f"{base_url}{start_page + page_number}"
    
    while True:
        response = requests.get(url)

        if response.status_code != 429:
            # Save the HTML content to a file
            filename = f"page_{start_page + page_number}.txt"
            with open(filename, "w", encoding="utf-8") as file:
                file.write(response.text)

            print(f"Downloaded page {page_number}/{num_pages}")
            break
        
        print(f"Received 429 error. Pausing for 2 seconds and retrying page {page_number}/{num_pages}...")
        time.sleep(8)

# Create a thread pool with a maximum of 4 worker threads
with ThreadPoolExecutor(max_workers=4) as executor:
    # Submit tasks to the thread pool
    futures = [executor.submit(download_page, page_number) for page_number in range(num_pages)]

    # Wait for all the tasks to complete
    for future in futures:
        future.result()

print("All pages downloaded successfully.")
