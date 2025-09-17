# Craigslist Crawler Python

A Python-based web crawler for scraping apartment listings from Craigslist across multiple European cities.

## Author

**Reza Mobaraki**
- GitHub: [@rezamobaraki](https://github.com/rezamobaraki)
- LinkedIn: [reza-mobaraki](https://linkedin.com/in/reza-mobaraki)

## Features

- **Multi-city crawling**: Supports multiple European cities (Paris, Berlin, Amsterdam, Munich)
- **Link extraction**: Efficiently finds and collects apartment listing URLs
- **Data extraction**: Parses detailed information from individual listings including:
  - Title and price
  - Post content/description
  - Publication date
  - Image URLs
- **Flexible storage**: Supports both MongoDB and file-based storage
- **Image downloading**: Downloads images from listings
- **Modular design**: Object-oriented architecture with separate crawler classes

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rezamobaraki/craigslist-crawler-python.git
cd craigslist-crawler-python
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Configure MongoDB (optional):
   - Install and start MongoDB
   - Update the connection settings in `mongo.py` if needed

## Configuration

Edit `config.py` to customize:
- **BASE_LINK**: Craigslist URL pattern for different cities
- **STORAGE_TYPE**: Choose between 'mongo' (MongoDB) or 'file' (JSON files)

```python
STORAGE_TYPE = 'mongo'  # Choices: 'mongo' or 'file'
```

## Usage

### Command Line Interface

The crawler provides three main operations:

#### 1. Find and collect listing links:
```bash
python main.py find_links
```

#### 2. Extract detailed data from collected links:
```bash
python main.py extract_pages
```

#### 3. Download images from listings:
```bash
python main.py download_images
```

### Functional Approach

Alternatively, use the functional crawler:

```bash
python functional_crawler.py find_links
python functional_crawler.py extract_pages
```

### Programmatic Usage

```python
from crawl import LinkCrawler, DataCrawler, ImageDownloader

# Find apartment listing links
crawler = LinkCrawler(cities=['paris', 'berlin', 'amsterdam', 'munich'])
links = crawler.start(store=True)

# Extract detailed data
data_crawler = DataCrawler()
data_crawler.start(store=True)

# Download images
image_downloader = ImageDownloader()
image_downloader.start(store=True)
```

## Project Structure

```
├── main.py              # Main entry point
├── crawl.py             # Core crawler classes
├── functional_crawler.py # Functional approach crawler
├── parser.py            # HTML parsing logic
├── storage.py           # Storage abstractions (MongoDB/File)
├── mongo.py             # MongoDB connection handling
├── config.py            # Configuration settings
├── requirements.txt     # Python dependencies
└── data/               # Output directory
    ├── adv/            # Advertisement JSON files
    └── images/         # Downloaded images
```

## Architecture

### Core Classes

- **CrawlerBase**: Abstract base class for all crawlers
- **LinkCrawler**: Finds and collects apartment listing URLs
- **DataCrawler**: Extracts detailed information from listings
- **ImageDownloader**: Downloads images from listings
- **AdvertisementPageParser**: Parses HTML content from individual listings
- **StorageAbstract**: Abstract storage interface
- **MongoStorage**: MongoDB storage implementation
- **FileStorage**: File-based JSON storage implementation

### Data Flow

1. **Link Collection**: Crawls Craigslist search pages to find apartment listing URLs
2. **Data Extraction**: Visits each listing URL to extract detailed information
3. **Storage**: Saves data to MongoDB or JSON files
4. **Image Download**: Downloads associated images for each listing

## Supported Cities

Currently configured for European cities:
- Paris
- Berlin  
- Amsterdam
- Munich

To add more cities, modify the `cities` parameter in `main.py` or when instantiating `LinkCrawler`.

## Output Format

### JSON Structure
```json
{
  "title": "Apartment Title",
  "price": "€500",
  "body": "Detailed description...",
  "post_id": "1234567890",
  "created_time": "2021-04-02T16:51:49+0200",
  "images": [
    {
      "url": "https://images.craigslist.org/...",
      "flag": false
    }
  ]
}
```

## Dependencies

- **requests**: HTTP requests handling
- **beautifulsoup4**: HTML parsing
- **selenium**: Web browser automation (if needed)
- **pymongo**: MongoDB integration

## Legal Notice

This tool is for educational and research purposes only. Please respect Craigslist's terms of service and implement appropriate delays between requests to avoid overwhelming their servers.

## License

MIT License - see LICENCE.txt for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Contact

For questions or support, please reach out via:
- GitHub Issues: [Create an issue](https://github.com/rezamobaraki/craigslist-crawler-python/issues)
- LinkedIn: [reza-mobaraki](https://linkedin.com/in/reza-mobaraki)