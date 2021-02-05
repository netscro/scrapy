import scrapy

from work_ua.items import PeopleItem


class WorkuaSpider(scrapy.Spider):
    name = 'workua'
    allowed_domains = ['work.ua']
    start_urls = ['https://www.work.ua/ru/resumes-kharkiv/']

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
            people_item['name'] = name
            people_item['age'] = age
            people_item['profession'] = profession

            # возвращаем по одному человеку через генератор
            yield people_item
