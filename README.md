# Craigslist Crawler Python

A Python-based web crawler for extracting real estate listings from Craigslist across multiple cities.

## Features

- Crawl Craigslist housing listings from multiple cities
- Extract advertisement data including titles, prices, and details
- Support for multiple storage backends (MongoDB, file storage)
- Image downloading capabilities
- Functional and object-oriented crawler implementations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rezamobaraki/craigslist-crawler-python.git
cd craigslist-crawler-python
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The crawler supports three main operations:

### 1. Find Links
Extract advertisement links from city pages:
```bash
python main.py find_links
```

### 2. Extract Page Data
Extract detailed data from advertisement pages:
```bash
python main.py extract_pages
```

### 3. Download Images
Download images from advertisements:
```bash
python main.py download_images
```

## Configuration

Modify `config.py` to adjust:
- Base URL patterns
- Storage type (MongoDB or file storage)
- Other crawler settings

## Storage Options

- **MongoDB**: Requires a running MongoDB instance
- **File Storage**: Saves data to local JSON files

## Project Structure

```
craigslist-crawler-python/
├── main.py                    # Main entry point
├── crawl.py                   # Core crawler classes
├── functional_crawler.py      # Functional approach implementation
├── parser.py                  # HTML parser for advertisement pages
├── storage.py                 # Storage backends (MongoDB/File)
├── mongo.py                   # MongoDB connection management
├── config.py                  # Configuration settings
├── requirements.txt           # Python dependencies
├── data/                      # Data storage directory
│   ├── adv/                   # Advertisement data
│   └── images/                # Downloaded images
└── README.md                  # This file
```

## Dependencies

- `requests` - HTTP library for web requests
- `beautifulsoup4` - HTML parsing
- `selenium` - Web browser automation (optional)
- `pymongo` - MongoDB driver

## Examples

### Basic Usage
```python
from crawl import LinkCrawler, DataCrawler

# Find links in specific cities
crawler = LinkCrawler(cities=['paris', 'berlin', 'amsterdam', 'munich'])
links = crawler.start(store=True)

# Extract data from found links
data_crawler = DataCrawler()
data_crawler.start(store=True)
```

### Functional Approach
```python
import functional_crawler

# Use the functional implementation
functional_crawler.start_crawl()
```

## Notes

- This crawler is for educational purposes only
- Respect Craigslist's robots.txt and terms of service
- Use reasonable delays between requests to avoid overloading servers
- The crawler currently supports European Craigslist sites

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Author

**Reza Mobaraki**
- GitHub: [@rezamobaraki](https://github.com/rezamobaraki)
- LinkedIn: [reza-mobaraki](https://linkedin.com/in/reza-mobaraki)

## License

This project is licensed under the MIT License - see the [LICENCE.txt](LICENCE.txt) file for details.
