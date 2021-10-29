# RSS-reader
## Description
RSS reader is a command-line utility which receives RSS URL and prints results in human-readable format.
## Formats
### Console output
```bash
$ rss_reader.py "https://news.yahoo.com/rss/" --limit 1

Feed: Yahoo News - Latest News & Headlines
Title: With latest payout, Arizona sheriff has cost taxpayers $100m
Link: https://news.yahoo.com/latest-payout-arizona-sheriff-cost-041238835.html
Date: Fri, 29 Oct 2021 04:12:38
Source: Associated Press
Source URL: http://www.ap.org/
```
### JSON output
```bash
$ rss_reader.py "https://news.yahoo.com/rss/" --limit 1 --json
```
#### news.json
```
[
  {
    "Feed": "Yahoo News - Latest News & Headlines",
    "Title": "With latest payout, Arizona sheriff has cost taxpayers $100m",
    "Link": "https://news.yahoo.com/latest-payout-arizona-sheriff-cost-041238835.html",
    "Date": "Fri, 29 Oct 2021 04:12:38",
    "Source": "Associated Press",
    "Source URL": "http://www.ap.org/"
  }
]
```
## Usage
```
usage: rss_reader.py [-h] [--version] [--json] [--verbose] [--limit LIMIT] [url]

positional arguments:
  url            URL

optional arguments:
  -h, --help     show this help message and exit
  --version      Prints version info
  --json         Prints result as JSON in stdout
  --verbose      Outputs verbose status messages
  --limit LIMIT  Limit news topics if this parameter provided
```
## Distribution
```
> pip install --editable .
```
### Note
Run this command from program folder
### Execution
#### With CLI
```
> rss_reader [url] [-h] [--version] [--json] [--verbose] [--limit LIMIT]
```
#### Whithout CLI
```
> python rss_reader.py [url] [-h] [--version] [--json] [--verbose] [--limit LIMIT]
```