#### Project Description:
The goal of this project is to use `Scrapy`, a powerful web **crawling** framework in `Python`, to crawl a list of websites and **analyze their popularity** based on specific metrics. The project will involve extracting relevant data such as page views, social media shares, backlinks, or other engagement indicators to determine the popularity of each website.

Key Features:
- **Web Crawling:** Use Scrapy to crawl a predefined list of websites.
- **Data Extraction:** Extract relevant data points (e.g., page titles, meta descriptions, social media links, etc.).
- **Popularity Analysis:** Analyze the extracted data to rank websites based on popularity metrics.
- **Output:** Save the results in a structured format (e.g., CSV, JSON, or database) for further analysis.

#### List of Websites to Crawl (Example):  
websites = [  
    "https://www.example.com",  
    "https://www.anotherexample.com",  
    "https://www.samplewebsite.com",  
    "https://www.testwebsite.com",  
    "https://www.demosite.com",  
]

Next Steps:  
Replace the example websites with your target list.  
Define the specific data points to extract for popularity analysis.  
Implement the Scrapy spider to crawl and extract data.  
Develop the popularity ranking logic based on the extracted data.  
Let me know if you need help with the Scrapy implementation or any other part of the project!

#### Dependencis
- python3.10
- scrapy

#### Create And Activate Environment
```bash
$ virtualenv -p python3.10 venv
$ source venv/bin/activate
```

#### Installation
```bash
$ pip install -r requirements.txt
```

#### Run

--- 

### Development
#### Create New Project
```bash
$ scrapy startproject popularity_analysis
```
