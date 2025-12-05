# Web Scraping Projects

A collection of web scraping utilities and projects demonstrating data collection from various web sources.

## Projects Included

### web_scraping.py

General-purpose web scraping utility featuring:

- HTML parsing with Beautiful Soup
- HTTP requests with error handling
- Retry logic and exponential backoff
- User-agent rotation
- Session management
- Data export capabilities
- Robots.txt compliance

**Usage:**

```python
from web_scraping import WebScraper

scraper = WebScraper()
data = scraper.scrape(url='https://example.com', selectors={'title': 'h1'})
```

### web_project0/

YouTube Analytics project using Jupyter Notebooks:

- `1_clinic_data.ipynb` - Healthcare data analysis
- `2_download_image.ipynb` - Image downloading utilities
- `2_youtube_views.ipynb` & `4_youtube_views.ipynb` - YouTube view analytics
- Includes sample data: `youtube_views.csv`

**Features:**

- Data collection and parsing
- Visualization with Matplotlib
- Statistical analysis
- Export capabilities

### web_project1/

Indian Stock Market Intelligence System - A comprehensive data pipeline for financial sentiment analysis:

**Features:**

- Mock data collection with configurable parameters
- Data processing pipeline using Pandas and Parquet
- Sentiment analysis on financial tweets
- Visualization of sentiment distribution
- Modular architecture (collection, processing, analysis)
- Logging integration
- Data export to Parquet format
- PNG visualization generation

**Project Structure:**

```
web_project1/
├── data/
│   ├── processed_tweets.parquet
│   └── sentiment_distribution.png
├── src/
│   ├── __init__.py
│   ├── analysis/
│   │   ├── __init__.py
│   │   └── analyzer.py
│   ├── collection/
│   │   ├── __init__.py
│   │   └── collector.py
│   ├── processing/
│   │   ├── __init__.py
│   │   └── processor.py
│   └── main.py
├── README.md
└── requirements.txt
```

**How to Run:**

```bash
cd web_project1
python src/main.py
```

---

## Requirements

```
beautifulsoup4>=4.12.0
requests>=2.31.0
pandas>=2.0.0
pyarrow>=12.0.0
matplotlib>=3.7.0
scikit-learn>=1.3.0
```

## Installation

```bash
pip install beautifulsoup4 requests pandas pyarrow matplotlib scikit-learn
```

## Legal Considerations

- Always check website's `robots.txt` file
- Respect rate limiting and use delays between requests
- Review website's Terms of Service before scraping
- Use appropriate User-Agent headers
- Consider using official APIs when available

## Performance

- **Average Request Time:** 0.5-3 seconds per page
- **Memory Usage:** Depends on data size
- **Concurrent Requests:** Recommended 5-10 threads max

---

**Last Updated:** December 2025
