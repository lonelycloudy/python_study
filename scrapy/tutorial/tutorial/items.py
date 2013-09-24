# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class TutorialItem(Item):
    # define the fields for your item here like:
    # name = Field()
	title = Field()
	link = Field()
	author = Field()
	click = Field()
	reply = Field()
	ftime = Field()
class TechSinaComment(Item):
	newsid = Field()
	comments = Field()
	test = Field()
	#content = Field()
	#nick = Field()
	#config = Field()
	#uid = Field()
	#parent = Field()
	#thread = Field()
	