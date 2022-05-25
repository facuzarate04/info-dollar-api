# info-dollar-api
This is my personal api used in my Amazon Alexa to ask about dollar price i usually search on specific web

## Langujes and Frameworks
- Python
- Flask

## Install Dependencies
- `pip install python-dotenv`
- `pip install beautifulsoup`
- `pip install flask-restful`

## Usage
### Oficial dollar
- `GET /oficial/all` Get all scraped information
- `GET /oficial/title` Get table data title
- `GET /oficial/date` Get information date
- `GET /oficial/buy` Get buy price
- `GET /oficial/sell` Get sell price
- `GET /oficial/variation` Get variation between las updated information
### Blue dollar
- `GET /blue/all` Get all scraped information
- `GET /blue/title` Get table data title
- `GET /blue/date` Get information date
- `GET /blue/buy` Get buy price
- `GET /blue/sell` Get sell price
- `GET /blue/variation` Get variation between las updated information
