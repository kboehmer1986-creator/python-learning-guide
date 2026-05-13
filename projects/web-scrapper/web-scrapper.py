# This program demonstrates web scraping using requests and BeautifulSoup.
# Note: Always respect websites terms of service when scraping.

import requests
from bs4 import BeautifulSoup
import csv
import json
from urllib.parse import urljoin, urlparse
import time
from typing import List, Dict, Optional

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
    for link in soup.find_all('a', href=True):
        href = link['href']
        # Skip empty, javascript, and mailto links
        if href.startswith(('javascript:', 'mailto:', '#')):
            continue
        # Join relative URLs with base URL
        absolute_url = urljoin(base_url, href)
        links.append(absolute_url)
    return links

def extract_headlines(soup: BeautifulSoup) -> List[str]:
    """
    Extract headlines (h1, h2, h3) from a webpage.

    Args:
        soup (BeautifulSoup): Parsed HTML content.

    Returns:
        List[str]: List of headlines.
    """
    headlines = []
    for i in range(1, 4):  # h1, h2, h3
        for headline in soup.find_all(f'h{i}'):
            headlines.append(headline.get_text().strip())
    return headlines

def extract_paragraphs(soup: BeautifulSoup) -> List[str]:
    """
    Extract paragraphs from a webpage.

    Args:
        soup (BeautifulSoup): Parsed HTML content.

    Returns:
        List[str]: List of paragraph texts.
    """
    paragraphs = []
    for p in soup.find_all('p'):
        text = p.get_text().strip()
        if text:  # Skip empty paragraphs
            paragraphs.append(text)
    return paragraphs

def extract_images(soup: BeautifulSoup, base_url: str) -> List[Dict[str, str]]:
    """
    Extract images from a webpage.

    Args:
        soup (BeautifulSoup): Parsed HTML content.
        base_url (str): Base URL to resolve relative image paths.

    Returns:
        List[Dict[str, str]]: List of dictionaries with image info (src, alt).
    """
    images = []
    for img in soup.find_all('img'):
        src = img.get('src', '')
        alt = img.get('alt', '')
        if src:
            absolute_src = urljoin(base_url, src)
            images.append({'src': absolute_src, 'alt': alt})
    return images

def scrape_website(url: str) -> Dict[str, any]:
    """
    Scrape a website and extract various elements.

    Args:
        url (str): URL of the website to scrape.

    Returns:
        Dict[str, any]: Dictionary containing extracted data.
    """
    content = get_page_content(url)
    if not content:
        return {'error': 'Failed to fetch page content'}

    soup = parse_html(content)
    if not soup:
        return {'error': 'Failed to parse HTML'}

    data = {
        'url': url,
        'title': soup.title.string if soup.title else 'No title',
        'headlines': extract_headlines(soup),
        'paragraphs': extract_paragraphs(soup),
        'links': extract_links(soup, url),
        'images': extract_images(soup, url),
        'metadata': {
            'description': soup.find('meta', attrs={'name': 'description'})['content']
            if soup.find('meta', attrs={'name': 'description'}) else None,
            'keywords': soup.find('meta', attrs={'name': 'keywords'})['content']
            if soup.find('meta', attrs={'name': 'keywords'}) else None
        }
    }

    return data

def save_to_csv(data: Dict[str, any], filename: str = 'scraped_data.csv') -> bool:
    """
    Save scraped data to a CSV file.

    Args:
        data (Dict[str, any]): Data to save.
        filename (str): Name of the CSV file.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)

            # Write header
            writer.writerow(['Type', 'Content'])

            # Write headlines
            for headline in data.get('headlines', []):
                writer.writerow(['Headline', headline])

            # Write paragraphs
            for paragraph in data.get('paragraphs', []):
                writer.writerow(['Paragraph', paragraph])

            # Write links
            for link in data.get('links', []):
                writer.writerow(['Link', link])

            # Write images
            for img in data.get('images', []):
                writer.writerow(['Image', f"{img['src']} - {img['alt']}"])

        return True
    except Exception as e:
        print(f"Error saving to CSV: {e}")
        return False

def save_to_json(data: Dict[str, any], filename: str = 'scraped_data.json') -> bool:
    """
    Save scraped data to a JSON file.

    Args:
        data (Dict[str, any]): Data to save.
        filename (str): Name of the JSON file.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving to JSON: {e}")
        return False

def scrape_multiple_pages(urls: List[str], delay: int = 2) -> List[Dict[str, any]]:
    """
    Scrape multiple webpages with a delay between requests.

    Args:
        urls (List[str]): List of URLs to scrape.
        delay (int): Delay in seconds between requests.

    Returns:
        List[Dict[str, any]]: List of scraped data for each URL.
    """
    results = []
    for url in urls:
        print(f"Scraping: {url}")
        data = scrape_website(url)
        results.append(data)
        time.sleep(delay)  # Respectful crawling
    return results

def display_scraped_data(data: Dict[str, any]) -> None:
    """
    Display scraped data in a readable format.

    Args:
        data (Dict[str, any]): Scraped data to display.
    """
    print(f"\n=== Scraped Data for: {data.get('url', 'Unknown URL')} ===")
    print(f"Title: {data.get('title', 'No title')}")

    print("\nHeadlines:")
    for i, headline in enumerate(data.get('headlines', []), 1):
        print(f"{i}. {headline}")

    print("\nFirst 3 Paragraphs:")
    for i, paragraph in enumerate(data.get('paragraphs', [])[:3], 1):
        print(f"{i}. {paragraph}")

    print(f"\nFound {len(data.get('links', []))} links")
    print(f"Found {len(data.get('images', []))} images")

    if data.get('metadata'):
        print("\nMetadata:")
        if data['metadata'].get('description'):
            print(f"Description: {data['metadata']['description']}")
        if data['metadata'].get('keywords'):
            print(f"Keywords: {data['metadata']['keywords']}")

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
                else:
                    print(f"Error scraping {data.get('url', 'a URL')}: {data['error']}")

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