# easy_scrape

This package makes scraping the web easier. Avaible method table, scrapes any table with a class name from the web. If the table tag is without a class, just supply the closest div to the method.

There can be multiple tables with a class name, so need to provide the table number.


## Prerequisites

selenium 3 - 
BeautifulSoup
requests
chrome webdriver

Use the requirements.txt file to install the prerequisites

### Installing

Use pip to install the package

- pip install easy_scrape

### Usage

```
from easy_scrape.scrape_table import scrape_table

scrape_obj = scrape_table(#pass the path of webdriver exe )

#with the below class names there are two tbales, so a pop up will ask you which one you want to scrape (expects a number)

list_of_basketball_winners = scrape_obj.table(url = 'https://en.wikipedia.org/wiki/List_of_NBA_champions', class_name = 'wikitable sortable jquery-tablesorter')


```

## Contributing

I would love to see a pull requests for improving this package in terms of speed, bugs and for covering other data points also.

