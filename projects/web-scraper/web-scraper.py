# This program demonstrates web scraping using requests and BeautifulSoup.
# Note: Always respect website's robots.txt and terms of service when scraping.

import requests
from bs4 import BeautifulSoup
import csv
import json
from urllib.parse import urljoin, urlparse
import time
from typing import List, Dict, Optional, Union

# User-Agent header to mimic a browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def is_valid_url(url: str) -> bool:
    """
    Check if a URL is valid.

    Args:
        url (str): URL to validate.

    Returns:
        bool: True if URL is valid, False otherwise.
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def get_page_content(url: str, timeout: int = 10) -> Optional[str]:
    """
    Fetch the content of a webpage.

    Args:
        url (str): URL of the webpage.
        timeout (int): Timeout in seconds.

    Returns:
        Optional[str]: Page content if successful, None otherwise.
    """
    if not is_valid_url(url):
        print(f"Invalid URL: {url}")
        return None
    try:
        response = requests.get(url, headers=HEADERS, timeout=timeout)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_html(content: str) -> Optional[BeautifulSoup]:
    """
    Parse HTML content using BeautifulSoup.

    Args:
        content (str): HTML content to parse.

    Returns:
        Optional[BeautifulSoup]: Parsed HTML if successful, None otherwise.
    """
    if not content:
        return None
    return BeautifulSoup(content, 'html.parser')

def extract_links(soup: BeautifulSoup, base_url: str) -> List[str]:
    """
    Extract all links from a webpage.

    Args:
        soup (BeautifulSoup): Parsed HTML content.
        base_url (str): Base URL to resolve relative links.

    Returns:
        List[str]: List of absolute URLs.
    """
    links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        # Resolve relative URLs
        absolute_url = urljoin(base_url, href)
        links.append(absolute_url)
    return links

def extract_text(soup: BeautifulSoup) -> str:
    """
    Extract all text content from a webpage.

    Args:
        soup (BeautifulSoup): Parsed HTML content.

    Returns:
        str: Extracted text content.
    """
    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()
    return soup.get_text(separator='\n', strip=True)

def extract_metadata(soup: BeautifulSoup) -> Dict[str, str]:
    """
    Extract metadata from a webpage.

    Args:
        soup (BeautifulSoup): Parsed HTML content.

    Returns:
        Dict[str, str]: Dictionary containing metadata.
    """
    metadata = {}

    # Extract title
    if soup.title:
        metadata['title'] = soup.title.string

    # Extract meta tags
    for meta in soup.find_all('meta'):
        if meta.get('name'):
            metadata[meta['name']] = meta.get('content', '')
        elif meta.get('property'):
            metadata[meta['property']] = meta.get('content', '')

    # Extract description
    if 'description' in metadata:
        metadata['description'] = metadata['description']
    elif soup.find('meta', attrs={'name': 'description'}):
        metadata['description'] = soup.find('meta', attrs={'name': 'description'})['content']

    # Extract keywords
    if 'keywords' in metadata:
        metadata['keywords'] = metadata['keywords']
    elif soup.find('meta', attrs={'name': 'keywords'}):
        metadata['keywords'] = soup.find('meta', attrs={'name': 'keywords'})['content']

    return metadata

def scrape_website(url: str) -> Dict[str, Union[str, List[str], Dict[str, str]]]:
    """
    Scrape a single webpage and extract its content.

    Args:
        url (str): URL of the webpage to scrape.

    Returns:
        Dict: Dictionary containing scraped data or error message.
    """
    if not is_valid_url(url):
        return {'error': 'Invalid URL'}

    content = get_page_content(url)
    if not content:
        return {'error': f'Failed to fetch content from {url}'}

    soup = parse_html(content)
    if not soup:
        return {'error': 'Failed to parse HTML content'}

    data = {
        'url': url,
        'text': extract_text(soup),
        'links': extract_links(soup, url),
        'metadata': extract_metadata(soup)
    }

    return data

def display_scraped_data(data: Dict) -> None:
    """
    Display the scraped data in a readable format.

    Args:
        data (Dict): Dictionary containing scraped data.
    """
    if 'error' in data:
        print(f"Error: {data['error']}")
        return

    print(f"\nURL: {data['url']}")
    if data['metadata'].get('title'):
        print(f"Title: {data['metadata']['title']}")
    if data['metadata'].get('description'):
        print(f"Description: {data['metadata']['description']}")
    if data['metadata'].get('keywords'):
        print(f"Keywords: {data['metadata']['keywords']}")

    print(f"\nText Content (first 200 characters):\n{data['text'][:200]}...")

    print(f"\nFound {len(data['links'])} links:")
    for i, link in enumerate(data['links'][:5], 1):  # Display first 5 links
        print(f"{i}. {link}")
    if len(data['links']) > 5:
        print(f"... and {len(data['links']) - 5} more links.")

def save_to_csv(data: Dict, filename: str = 'scraped_data.csv') -> bool:
    """
    Save scraped data to a CSV file.

    Args:
        data (Dict): Dictionary containing scraped data.
        filename (str): Name of the CSV file.

    Returns:
        bool: True if successful, False otherwise.
    """
    if 'error' in data:
        print(f"Cannot save data with error: {data['error']}")
        return False

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['URL', 'Title', 'Description', 'Keywords', 'Text', 'Links'])

            title = data['metadata'].get('title', '')
            description = data['metadata'].get('description', '')
            keywords = data['metadata'].get('keywords', '')
            text = data['text']
            links = '; '.join(data['links'])

            writer.writerow([data['url'], title, description, keywords, text, links])
        return True
    except Exception as e:
        print(f"Error saving to CSV: {e}")
        return False

def save_to_json(data: Dict, filename: str = 'scraped_data.json') -> bool:
    """
    Save scraped data to a JSON file.

    Args:
        data (Dict): Dictionary containing scraped data.
        filename (str): Name of the JSON file.

    Returns:
        bool: True if successful, False otherwise.
    """
    if 'error' in data:
        print(f"Cannot save data with error: {data['error']}")
        return False

    try:
        with open(filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving to JSON: {e}")
        return False

def scrape_multiple_pages(urls: List[str], delay: int = 2) -> List[Dict]:
    """
    Scrape multiple webpages with a delay between requests.

    Args:
        urls (List[str]): List of URLs to scrape.
        delay (int): Delay between requests in seconds.

    Returns:
        List[Dict]: List of dictionaries containing scraped data.
    """
    results = []
    for url in urls:
        print(f"\nScraping: {url}")
        data = scrape_website(url)
        results.append(data)
        time.sleep(delay)  # Respectful crawling
    return results

def main():
    """Main function to run the web scraper."""
    print("=== Web Scraper ===")
    print("1. Scrape a single webpage")
    print("2. Scrape multiple webpages")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        url = input("Enter the URL to scrape: ").strip()
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        data = scrape_website(url)
        if 'error' in data:
            print(f"Error: {data['error']}")
        else:
            display_scraped_data(data)
            # Save options
            save_format = input("\nSave data to file? (csv/json/n): ").lower()
            if save_format == 'csv':
                filename = input("Enter CSV filename (default: scraped_data.csv): ") or 'scraped_data.csv'
                if save_to_csv(data, filename):
                    print(f"Data saved to {filename}")
            elif save_format == 'json':
                filename = input("Enter JSON filename (default: scraped_data.json): ") or 'scraped_data.json'
                if save_to_json(data, filename):
                    print(f"Data saved to {filename}")

    elif choice == '2':
        urls = []
        print("Enter URLs to scrape (one per line, empty line to finish):")
        while True:
            url = input("URL: ").strip()
            if not url:
                break
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            urls.append(url)
        if urls:
            delay = int(input("Enter delay between requests (seconds, default 2): ") or 2)
            results = scrape_multiple_pages(urls, delay)
            for data in results:
                if 'error' not in data:
                    display_scraped_data(data)
            # Save all results
            save_format = input("\nSave all data to file? (csv/json/n): ").lower()
            if save_format == 'json':
                filename = input("Enter JSON filename (default: scraped_data.json): ") or 'scraped_data.json'
                # Combine all results into one dictionary
                combined_data = {'pages': results}
                if save_to_json(combined_data, filename):
                    print(f"All data saved to {filename}")
        else:
            print("No URLs entered.")

    elif choice == '3':
        print("Exiting the web scraper. Goodbye!")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    # Example usage (commented out)
    # url = "https://example.com"
    # data = scrape_website(url)
    # display_scraped_data(data)
    # save_to_json(data, "example.json")
    # Run the main interactive program
    main()
