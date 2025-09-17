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

## Author

**Reza Mobaraki**
- GitHub: [@rezamobaraki](https://github.com/rezamobaraki)
- LinkedIn: [reza-mobaraki](https://linkedin.com/in/reza-mobaraki)

## License

This project is licensed under the MIT License - see the [LICENCE.txt](LICENCE.txt) file for details.
