import scrapy
import json

from popularity_analysis.items import PopularityAnalysisItem


class Varzesh3Spider(scrapy.Spider):
    name = 'varzesh3'
    allowed_domains = ['varzesh3.com', 'web-api.varzesh3.com']

    custom_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Origin': 'https://www.varzesh3.com',
        'Connection': 'keep-alive',
        'Referer': 'https://www.varzesh3.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'TE': 'trailers'
    }

    def start_requests(self):
        base_url = 'https://web-api.varzesh3.com/v1.0/news/archive'
        params = {
            'to': '1742490459',
            'skip': '0',
            'take': '20'
        }
        first_url = f"{base_url}?to={params['to']}&skip={params['skip']}&take={params['take']}"
        self.logger.info(f"Starting with URL: {first_url}")
        yield scrapy.Request(
            url=first_url,
            headers=self.custom_headers,
            callback=self.parse,
            errback=self.handle_error
        )

    def parse(self, response):
        self.logger.info(f"Response received: {response.url} - Status: {response.status}")
        
        if response.status != 200:
            self.logger.error(f"Non-200 response: {response.status} - {response.text}")
            return

        try:
            data = json.loads(response.text)
            self.logger.info(f"JSON parsed successfully: {len(data.get('items', []))} items found")
        except json.JSONDecodeError as e:
            self.logger.error(f"JSON decode error: {e} - Response: {response.text}")
            return

        items = data.get('items', [])
        if not items:
            self.logger.warning("No items found in response")
            return

        for news in items:
            item = PopularityAnalysisItem()
            item['title'] = news.get('title')
            item['content'] = news.get('summary') or news.get('description')
            item['url'] = news.get('url') or news.get('link')
            item['date'] = news.get('date') or news.get('publishedDate')
            item['source'] = 'varzesh3'
            yield item

        current_skip = int(response.url.split('skip=')[1].split('&')[0])
        take = int(response.url.split('take=')[1])
        next_skip = current_skip + take
        next_url = f"https://web-api.varzesh3.com/v1.0/news/archive?to=1742490459&skip={next_skip}&take={take}"
        
        self.logger.info(f"Next request: {next_url}")
        yield scrapy.Request(
            url=next_url,
            headers=self.custom_headers,
            callback=self.parse,
            errback=self.handle_error
        )

    def handle_error(self, failure):
        self.logger.error(f"Request failed: {failure}")
