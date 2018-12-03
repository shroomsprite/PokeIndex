import scrapy


class PokeBall(scrapy.Spider):
	name = "PokeBall"

	def start_requests(self):
		urls = [
		'https://wiki.52poke.com/wiki/%E5%A6%99%E8%9B%99%E7%A7%8D%E5%AD%90',
		]
		
		for url in urls:
			yield scrapy.Request(url = url, callback=self.parse)

	def parse(self, response):
		filename = 'test.html'
		with open(filename, 'wb') as f:
			f.write(response.body)  
