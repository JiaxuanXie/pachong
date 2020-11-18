import scrapy
import json
from douyuSpider.items import DouyuspiderItem

class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyu.com']
    base_url = 'https://m.douyu.com/api/room/list?page={}&type='
    page = 1
    start_urls = [base_url.format(page)]

    def parse(self, response):
        data_list = json.loads(response.body)['data']
        if len(data_list['list']) == 0:
            return  # 遇到return终止返回
        for data in data_list['list']:
            item = DouyuspiderItem()
            item['nickname'] = data['nickname'].encode('utf-8')  # 防止中文出现乱码，进行utf-8编码
            item['roomSrc'] = data['roomSrc']
            item['hn'] = data['hn']
            yield item   # yield迭代器

        self.page += 1
        url = self.base_url.format(self.page)

        yield scrapy.Request(url, callback=self.parse)  # 回调函数不用加括号()




