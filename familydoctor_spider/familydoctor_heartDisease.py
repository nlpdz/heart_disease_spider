# -*- coding: utf-8 -*-
import re
import requests
import json
import os


id_data = []  #存放所有id

for page_id in range(1, 200):
    try:
        page_url = 'http://ask.39.net/browse/19-1-%d.html' % page_id
        headers = {

                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
                'Referer': 'http://ask.39.net/browse/19-1-%d.html' % page_id
            }
        r = requests.get(page_url, headers=headers)
        # print(r.text)
        r.encoding = ('utf-8')
        html = r.text
        # lis = re.findall(r'<a href="/question/[0-9]+.html">', html, re.S)
        # lis = set(lis)

        ids = re.findall(r'<a href="/question/(\d+).html', html)
        ids = set(ids)
        for i in ids:
            id_data.append(int(i))
            url = 'http://ask.39.net/question/%d.html' % int(i)
            try:
                r = requests.get(url, headers=headers)
                r.encoding = ('utf-8')
                html = r.text
                lis_Q = re.findall(r'<p class="txt_ms">(.*?)</p>', html, re.S)
                for i in lis_Q:
                    try:
                        i = i.replace('\n', '')
                        i = i.replace('<br />', '')
                        i = i.replace('<br/>', '')
                        i = i.replace('<b>', '')
                        i = i.replace('</b>', '')
                        i = i.replace('问题补充：', '')
                        i = i.strip()
                    except:
                        pass
                    Q = i
                    break

                lis_A = re.findall(r'<p class="sele_txt">(.*?)</p>', html, re.S)
                for j in lis_A:
                    try:
                        j = j.replace('\n', '')
                        j = j.replace('<br />', '')
                        j = j.replace('<br/>', '')
                        j = j.replace('<span class="pingjia">', '')
                        j = j.replace('答案的评价：<br>ask6I51V：很对</span>', '')
                        j = j.replace('</span>', '')
                        j = j.strip()
                    except:
                        pass
                    A = j
                    break

                with open('QA.txt', 'a') as ff:
                    if len(Q) < 60 and len(A) < 100:
                        ff.write(Q)
                        ff.write('\n')
                        ff.write(A)
                        ff.write('\n')
                        ff.write('\n')
                        # print(Q)
                        # print(A)
                        # print('\n')

            except:
                pass
            print(id)

    except:
        pass

