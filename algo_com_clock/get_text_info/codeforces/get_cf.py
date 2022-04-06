#! /usr/bin/env python3
import requests
from lxml import etree
url = 'https://codeforces.com/contests?complete=true'
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
}


class CF_Spider:
    def __init__(self):
        pass

    def get_exam(self):
        exam_info_list = self.tree.xpath('//*[@id="pageContent"]/div[1]/div[1]/div[6]/table//tr')
        exam_list = []
        skip = True
        for exam in exam_info_list:
            if skip:
                skip = False
                continue

            #id
            #考试名
            exam_name = self.tree.xpath('./')


    def main(self):
        # 获取页面源码
        response = requests.get(url=url, headers=headers)

        page_text = response.text
        # print(page_text)

        self.tree = etree.HTML(page_text)


# 获取页面源码
response = requests.get(url=url, headers=headers)

page_text = response.text
# print(page_text)

tree = etree.HTML(page_text)
# exam = tree.xpath('//tbody')[0]
exam = tree.xpath('//*[@id="pageContent"]/div[1]/div[1]/div[6]/table//tr[2]/td[3]/a/text()')
print(exam)
