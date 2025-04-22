# web-scraper

A simple Python-based web scraping toolkit.

## Features
- Input a URL to get the web page title.
- Batch scrape multiple URLs and save results to a file.
- Designed for easy extension to more advanced scraping features in the future.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

**Default test (no arguments):**
```bash
python scraper.py
```

**Scrape a single URL:**
```bash
python scraper.py https://www.example.com
```

**Batch scrape multiple URLs and save results:**
```bash
python scraper.py https://www.example.com https://www.python.org https://www.github.com
```
The results will be saved to `titles.txt`.

## Packaging for Release

```bash
python setup.py sdist
```

## Contributing & Upgrading
- Contributions (issues and pull requests) are welcome.
- The project is actively maintained and open for new scraping and parsing features.

---

Author: hopelee8964
