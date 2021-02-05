import scrapy


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
            # print(name, str(age).replace('·', 'None'), profession)

            yield {
                'name': name,
                'age': str(age).replace('\xa0', ' '),
                'profession': profession
            }
