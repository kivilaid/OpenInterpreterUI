import requests

def download_link_to_txt(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Checks if the request was successful

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)
        return f"Downloaded and saved as {filename}"
    except requests.RequestException as e:
        return f"Error with {url}: {e}"

# List of URLs to download
urls = [
    'https://www.riigiteataja.ee/akt/108122023006.txt',
    

    
]

# Loop through each URL and download content
for i, url in enumerate(urls, start=1):
    filename = f'output_{i}.txt'  # Creates a unique filename for each URL
    result = download_link_to_txt(url, filename)
    print(result)
