# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'text': quote.css("span.text::text").extract_first(),
                'author': quote.css("small.author::text").extract_first(),
                'tags': quote.css("div.tags > a.tag::text").extract()
            }

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))


class FlohScraper(scrapy.Spider):
    name = "flohscraper"
    start_urls = [
        f"https://www.flohmarkt.at/flohmaerkte/wien/{i}"
        for i in range(0, 121, 15)
    ]

    even_titles = [
        f"td:nth-child(1) div:nth-child(1) div.terminBox:nth-child({i}) div.terminTitel:nth-child(2) > a:nth-child(1)::text"
                     for i in range(2, 17, 2)
    ]
    odd_titles = [
        f"td:nth-child(1) div:nth-child(1) div:nth-child({i}) div.terminTitel:nth-child(2) > a:nth-child(1)::text"
                    for i in range(3, 17, 2)
    ]
    even_urls = [
        f"td:nth-child(1) div:nth-child(1) div.terminBox:nth-child({i}) div.terminTitel:nth-child(2) > a:nth-child(1)::href"
                     for i in range(2, 17, 2)
    ]
    odd_urls = [
        f"td:nth-child(1) div:nth-child(1) div:nth-child({i}) div.terminTitel:nth-child(2) > a:nth-child(1)::href"
                    for i in range(3, 17, 2)
    ]
    even_text = [
        f"td:nth-child(1) div:nth-child(1) div.terminBox:nth-child({i})::text"
                  for i in range(2, 17, 2)
    ]
    odd_text = [
        f"td:nth-child(1) div:nth-child(1) div:nth-child({i})::text"
        for i in range(3, 17, 2)
    ]

    titles = [*even_titles, *odd_titles]
    text = [*even_text, *odd_text]
    urls = [*even_urls, *odd_urls]

    def parse(self, response):
        for j, title in enumerate(self.titles):
            yield {
                'title': response.css(title).extract(),
                'date': response.css(self.text[j]).extract()[0].strip(),
                'short_info': response.css(self.text[j]).extract()[2].strip(),
                'url': response.css(self.urls[j]).extract()
            }
