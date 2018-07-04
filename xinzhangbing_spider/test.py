# -*- coding: utf-8 -*-
import re
import requests

id_data = []  #存放所有id

# for page_id in range(1, 51):
#     page_url = 'http://so.xywy.com/wenda.php?keyword=心脏病&src=so&page=%d' % page_id
#     print(page_url)
#     # headers = {
#     #
#     #         'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.0 Safari/534.13',
#     #         'Referer': 'http://so.xywy.com/wenda.php?keyword=%E5%BF%83%E8%84%8F%E7%97%85&src=so&page=%d' % page_id
#     #     }
#     r = requests.get(page_url)
#     # print(r.text)
#     r.encoding = ('utf-8')
#     html = r.text
#     print(html)

