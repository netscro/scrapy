# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class WorkUaItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PeopleItem(Item):
    name = Field()
    age = Field()
    profession = Field()
    detail_info = Field()
