"""
Craigslist Crawler - Configuration

Configuration settings for the Craigslist crawler application.

Author: Reza Mobaraki
GitHub: https://github.com/rezamobaraki
LinkedIn: https://linkedin.com/in/reza-mobaraki
"""

BASE_LINK = 'https://{}.craigslist.org/search/hhh?availabilityMode=0&sale_date' \
            '=all+data&s='

STORAGE_TYPE = 'mongo'  # Choices [ 'mongo', 'file' ]
