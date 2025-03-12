import scrapy


class SnpSpider(scrapy.Spider):
    name = "snp"
    allowed_domains = ["www.slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]
#i couldnt find the id in the source code anywhere. 
    def parse(self, response):
        rows = response.xpath("//*[@id=""]//td[1]/a/text()").get()
        company = response.xpath("//table[@id=""]//td[2]/a/text()").get()
        symbol = response.xpath("//table[@id=""]//td[3]/a/text()").get()
        ytd = response.xpath("//table[@id=""]//td[4]/a/text()").get()
        return {"number": number,
                "company": company,
                "symbol": symbol,
                "ytd": ytd}
