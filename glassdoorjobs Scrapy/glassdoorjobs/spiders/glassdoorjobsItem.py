from scrapy import Spider, Request
from glassdoorjobs.items import glassdoorjobsItem
import re

class GlassDoorSpider(Spider):
	name = "glassdoorjobs_spider"
	allowed_urls = ['https://www.glassdoor.com/index.htm']
	start_urls = ['https://www.glassdoor.com/Job/arkansas-data-science-jobs-SRCH_IL.0,8_IS1892_KO9,21_IP1.htm', 
 				'https://www.glassdoor.com/Job/california-data-science-jobs-SRCH_IL.0,10_IS2280_KO11,23_IP1.htm', 
				'https://www.glassdoor.com/Job/colorado-data-science-jobs-SRCH_IL.0,8_IS2519_KO9,21_IP1.htm', 
				'https://www.glassdoor.com/Job/connecticut-data-science-jobs-SRCH_IL.0,11_IS2697_KO12,24_IP1.htm', 
				'https://www.glassdoor.com/Job/delaware-data-science-jobs-SRCH_IL.0,8_IS3523_KO9,21_IP1.htm', 
				'https://www.glassdoor.com/Job/florida-data-science-jobs-SRCH_IL.0,7_IS3318_KO8,20_IP1.htm', 
				'https://www.glassdoor.com/Job/hawaii-data-science-jobs-SRCH_IL.0,6_IS1385_KO7,19_IP1.htm', 
				'https://www.glassdoor.com/Job/idaho-data-science-jobs-SRCH_IL.0,5_IS132_KO6,18_IP1.htm', 
				'https://www.glassdoor.com/Job/illinois-data-science-jobs-SRCH_IL.0,8_IS302_KO9,21_IP1.htm', 
				'https://www.glassdoor.com/Job/indiana-data-science-jobs-SRCH_IL.0,7_IS2124_KO8,20_IP1.htm', 
				'https://www.glassdoor.com/Job/iowa-data-science-jobs-SRCH_IL.0,4_IS2733_KO5,17_IP1.htm', 
				'https://www.glassdoor.com/Job/kansas-data-science-jobs-SRCH_IL.0,6_IS3107_KO7,19_IP1.htm', 
				'https://www.glassdoor.com/Job/kentucky-data-science-jobs-SRCH_IL.0,8_IS1141_KO9,21_IP1.htm', 
				'https://www.glassdoor.com/Job/louisiana-data-science-jobs-SRCH_IL.0,9_IS2792_KO10,22_IP1.htm', 
				'https://www.glassdoor.com/Job/maine-data-science-jobs-SRCH_IL.0,5_IS758_KO6,18_IP1.htm', 
				'https://www.glassdoor.com/Job/maryland-data-science-jobs-SRCH_IL.0,8_IS3201_KO9,21_IP1.htm', 
				'https://www.glassdoor.com/Job/massachusetts-data-science-jobs-SRCH_IL.0,13_IS3399_KO14,26_IP1.htm', 
				'https://www.glassdoor.com/Job/michigan-data-science-jobs-SRCH_IL.0,8_IS527_KO9,21_IP1.htm', 
				'https://www.glassdoor.com/Job/minnesota-data-science-jobs-SRCH_IL.0,9_IS1775_KO10,22_IP1.htm', 
				'https://www.glassdoor.com/Job/missouri-data-science-jobs-SRCH_IL.0,8_IS386_KO9,21_IP1.htm', 
				'https://www.glassdoor.com/Job/montana-data-science-jobs-SRCH_IL.0,7_IS669_KO8,20_IP1.htm', 
				'https://www.glassdoor.com/Job/nebraska-data-science-jobs-SRCH_IL.0,8_IS792_KO9,21_IP1.htm', 
				'https://www.glassdoor.com/Job/nevada-data-science-jobs-SRCH_IL.0,6_IS2756_KO7,19_IP1.htm', 
				'https://www.glassdoor.com/Job/new-hampshire-data-science-jobs-SRCH_IL.0,13_IS2403_KO14,26_IP1.htm', 
				'https://www.glassdoor.com/Job/new-jersey-data-science-jobs-SRCH_IL.0,10_IS39_KO11,23_IP1.htm', 
				'https://www.glassdoor.com/Job/new-mexico-data-science-jobs-SRCH_IL.0,10_IS1181_KO11,23_IP1.htm', 
				'https://www.glassdoor.com/Job/new-york-data-science-jobs-SRCH_IL.0,14_IS428_KO15,29_IP1.htm', 
				'https://www.glassdoor.com/Job/north-carolina-data-science-jobs-SRCH_IL.0,14_IS1282_KO15,27_IP1.htm', 
				'https://www.glassdoor.com/Job/ohio-data-science-jobs-SRCH_IL.0,4_IS2235_KO5,17_IP1.htm', 
				'https://www.glassdoor.com/Job/oklahoma-data-science-jobs-SRCH_IL.0,8_IS847_KO9,21_IP1.htm', 
				'https://www.glassdoor.com/Job/oregon-data-science-jobs-SRCH_IL.0,6_IS3163_KO7,19_IP1.htm', 
				'https://www.glassdoor.com/Job/pennsylvania-data-science-jobs-SRCH_IL.0,12_IS3185_KO13,25_IP1.htm', 
				'https://www.glassdoor.com/Job/rhode-island-data-science-jobs-SRCH_IL.0,12_IS3156_KO13,25_IP1.htm', 
				'https://www.glassdoor.com/Job/south-carolina-data-science-jobs-SRCH_IL.0,14_IS3411_KO15,27_IP1.htm', 
				'https://www.glassdoor.com/Job/south-dakota-data-science-jobs-SRCH_IL.0,12_IS1502_KO13,25_IP1.htm', 
				'https://www.glassdoor.com/Job/tennessee-data-science-jobs-SRCH_IL.0,9_IS1968_KO10,22_IP1.htm', 
				'https://www.glassdoor.com/Job/texas-data-science-jobs-SRCH_IL.0,5_IS1347_KO6,18_IP1.htm', 
				'https://www.glassdoor.com/Job/utah-data-science-jobs-SRCH_IL.0,4_IS255_KO5,17_IP1.htm', 
				'https://www.glassdoor.com/Job/vermont-data-science-jobs-SRCH_IL.0,7_IS1765_KO8,20_IP1.htm', 
				'https://www.glassdoor.com/Job/virginia-data-science-jobs-SRCH_IL.0,8_IS323_KO9,21_IP1.htm',
				'https://www.glassdoor.com/Job/washington-state-data-science-jobs-SRCH_IL.0,16_IS3020_KO17,29_IP1.htm', 
				'https://www.glassdoor.com/Job/wisconsin-data-science-jobs-SRCH_IL.0,9_IS481_KO10,22_IP1.htm']

	def parse(self, response):
		# identify the number of pages. On this website #pages footer format is "Page 1 of XXXX". We are interested in "XXXX
		# Identify the xpath for this "Page 1 of XXXX"
		# copy and paste the xpath into response.xpath()
		# Test the Xpath in the scrapy shell: should return a selector element
		# We are interested in the text so we added "/text" to the xpath and extglassracted the content using .extract()method
		# returned a list with a string "Page 1 of 1042". We selected this string using [0] index. Split the string on empty spaces
		# extracted the last element which should be the last page number

		print('-'*100)
		page_number = int(response.xpath('//*[@id="ResultsFooter"]/div[1]/text()').extract()[0].split(" ")[-1])
		print (page_number)
		start_url = response.request.url
		#start_url = start_urls
		print('-'*100)
		print(start_url)
		print('-'*100)
		# Used list comprehension to make a list of all page numbers. Add one to the second argument in the range function
		following_urls = [start_url.replace('IP2',x) for x in ['IP{}'.format(i) for i in range(1,page_number)]]
		print (len(following_urls))
		print ('*'*50)


		for idx, url in enumerate(following_urls):
			print('Entering page ',idx)
			print('-'*100)
			print(url)
			print('-'*100)
			Request (url = url, callback = self.parse_following_jobs_page)
			print('-'*100)
			yield Request (url = url, callback = self.parse_following_jobs_page)

	def parse_following_jobs_page(self, response):

		job_links = response.xpath('//div[@class="flexbox jobTitle"]/div/a/@href').extract()
		item = glassdoorjobsItem()
		item['job_links'] = job_links
		yield item