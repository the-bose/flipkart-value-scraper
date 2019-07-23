# Flipkart Product Value Scraper
## Description
An app that scrapes the following flipkart product values:
* Product title
* Product price
* Total rating
* 'Value for money' rating
* Warranty of product (in months)

## Installation
Clone the repository

	git clone https://github.com/the-bose/flipkart-value-scraper.git
	cd flipkart-value-scraper
	
Install the required plugins

	pip install -r requirement.txt
	
## Running

	python app.py <flipkart-url>
	
### Example

	python app.py https://www.flipkart.com/realme-c2-diamond-black-16-gb/p/itmfgwbaahz6ph9j
  
## Output

	<price> <rating> <value-for-money> <warranty-in-months>
