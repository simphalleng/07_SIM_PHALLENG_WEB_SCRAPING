import scrapy

class MySpider(scrapy.Spider):
    name = 'firstscrap'
    start_urls = ['https://www.goldonecomputer.com/']

    def parse(self, response):
        titles = response.css('a.activSub::text').extract()
        types = response.css('h4 a::text').extract()

        product = []
        for title in titles:
            product.append({'title': title})
        for type_ in types:
            product.append({'type': type_})

        # Output to a JSON file
        yield {'product': product}
