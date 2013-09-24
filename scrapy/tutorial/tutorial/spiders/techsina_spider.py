#tech.sina.com.cn  code
#http://tech.sina.com.cn/t/2013-07-17/11438548320.shtml
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from tutorial.items import TechSinaComment
from scrapy.http import Request
import json

class DmozSpider(BaseSpider):
	name="techsina"
	allowed_domains = ["tech.sina.com.cn"]
	start_urls = [
		"http://tech.sina.com.cn/t/2013-07-17/11438548320.shtml"
	]
	def parsefile(self,response):
		filename = response.url.split("/")[-2]
		open(filename,'wb').write(response.body)
	def parse_item(self,response):
		#strs = json.dumps(dic)
		#strList = json.loads(strs)
		strList = json.loads(response)
		item = response.meta['item']
		item['comments'] = strList
		return item
	def parse(self,response):
		hxs = HtmlXPathSelector(response)
		items = []
		item = TechSinaComment()
		newsid = hxs.select('/html/head/meta[9]/@content').extract()
		item['newsid'] = newsid[0].replace(',','-')
		item['comments'] =  hxs.select('/html/head/script[40]/text()').extract()
		item['test'] = hxs.select('//*[@id="J_Comment_Wrap"]/@class').extract()
		url = 'http://comment5.news.sina.com.cn/page/info?format=json&channel=kj&newsid='+item['newsid']+'&group=0&compress=1&ie=gbk&oe=gbk&page=1&page_size=100'
		return [Request(url,meta={'item':item}, callback=self.parse_item)]
		#items.append(item)
		#return items
		
			