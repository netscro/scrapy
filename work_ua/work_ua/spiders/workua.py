from work_ua.items import PeopleItem

import scrapy
from scrapy import Request


class WorkuaSpider(scrapy.Spider):
    name = 'workua'
    allowed_domains = ['work.ua']
    start_urls = ['https://www.work.ua/ru/resumes-kharkiv/']
    site_url = 'https://www.work.ua'

    def parse(self, response):

        for person in response.css('div.card.resume-link'):
            name = person.css('div > b::text').get()

            age = person.css('div > span:nth-child(3)::text').get()
            if '\xa0' in str(age):
                age = str(age).replace('\xa0', ' ')
            else:
                age = str(age).replace('· ', 'None')

            profession = person.css('h2 > a::text').get()

            # структура json документа при помощи items.py
            people_item = PeopleItem()
            people_item['name'] = name.strip()
            people_item['age'] = age
            people_item['profession'] = profession

            # возвращаем по одному человеку через генератор
            # yield people_item

            # детальная информация работника
            detail_page = person.css('div.row div a::attr(href)').get()
            detail_page_url = self.site_url + detail_page
            yield Request(detail_page_url, self.parse_detail_info_page,
                          meta={
                              'people_item': people_item
                          })

        # переход по страницам пагинации
        # next_page = response.css('ul.pagination-small li a::attr(href)').getall() # noqa - E501 line too long
        # if next_page:
        #     next_url = self.site_url + next_page[-1]
        #     yield Request(next_url)

    def parse_detail_info_page(self, response):
        detail_info_url = response.css('p#addInfo::text').get()
        people_item = response.meta['people_item']
        people_item['detail_info'] = detail_info_url
        yield people_item
