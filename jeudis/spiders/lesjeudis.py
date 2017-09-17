# Used urls
# standard offer: https://www.lesjeudis.com/jdp/ing%C3%A9nieur-syst%C3%A8me-linux-h-f-jgx1hj6300gxh6ttsv0
# pp offer: https://www.lesjeudis.com/jdp/technicien-support-applicatif-h-f-j3k5pf60sgp2w3b3fkv

import scrapy

from jeudis.items import JobItem

class OfferSpider(scrapy.Spider):
    name = "lesjeudis"

    BASE_URL = 'https://www.lesjeudis.com'
    start_urls = ['https://www.lesjeudis.com/recherche?pg=1']

    def parse(self, response):
        job_links = response.css('a.job-title::attr(href)').extract()

        for job_link in job_links:
            job_link = self.BASE_URL+job_link
            yield scrapy.Request(
                job_link,
                callback=self.parser_router,
            )

        # when all offer links in the current page have been exploted, go to next page and start over
        if response.url == 'https://www.lesjeudis.com/recherche?pg=1':
            next_page_extension = response.css('a.btn-arrow::attr(href)').extract_first()
        else:
            next_page_extension = response.css('a.btn-arrow::attr(href)').extract()[1]
        next_page = self.BASE_URL+next_page_extension
        try:
            yield scrapy.Request(next_page, callback=self.parse)
        except Exception:
            self.logger.debug("Error when parsing next_page from url: {}").format(response.url)


    # parser_router's job is to route offers according to their html patterns
    def parser_router(self, response):
        url = response.url
        distinctive_element = response.xpath('//script[2]').extract_first()
        if '"company_name":"Page Personnel"' in distinctive_element:
            yield self.parse_pp_offer(response)
        else:
            yield self.parse_standard_offer(response)


    def parse_standard_offer(self, response):
        job = JobItem()

        job['domain'] = "www.lesjeudis.com"
        job['clean_url'] = response.url

        try:
            job['title'] = response.xpath('//h1/text()').extract_first().strip()
        except Exception:
            self.logger.debug("Error when parsing title from url: {}".format(response.url))
        try:
            job['company'] = response.xpath('//h1/span/text()').extract_first().strip()[10:]
        except Exception:
            self.logger.debug("Error when parsing company from url: {}".format(response.url))
        try:
            job['location'] = esponse.xpath('//*[@id="jdp"]/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/text()').extract()[1].strip()
        except Exception:
            self.logger.debug("Error when parsing location from url: {}".format(response.url))
        try:
            job['salary'] = response.xpath('//*[@id="jdp"]/div[2]/div/div/div[1]/div[3]/div[2]/div[1]/text()').extract()[1].strip()
        except Exception:
            self.logger.debug("Error when parsing salary from url: {}".format(response.url))
        try:
            job['type'] = response.xpath('//*[@id="jdp"]/div[2]/div/div/div[1]/div[3]/div[1]/div[1]/text()').extract()[1].strip()
        except Exception:
            self.logger.debug("Error when parsing type from url: {}".format(response.url))
        try:
            unstripped_tags = response.css('div.tags a.tag::text').extract()
            tags = [tag.strip() for tag in unstripped_tags]
            job['tags'] = tags
        except Exception:
            self.logger.debug("Error when parsing tags from url: {}".format(response.url))
        try:
            job["description_html"] = response.xpath('//div[@id="job-description"]'.extract_first())
        except Exception:
            self.logger.debug("Error when parsing description_html from url: {}".format(response.url))
        return job

    # currently not handled
    def parse_pp_offer(self, response):
        return
        job = JobItem()
        try:
            job["description_html"] = response.xpath('//div[@id="G_bloc2_MP"]').extract_first()
        except Exception:
            self.logger.debug("Error when parsing description_html from url: {}".format(response.url))
        return job
