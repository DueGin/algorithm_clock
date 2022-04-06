import requests
from lxml import etree
import json
url = 'https://ac.nowcoder.com/acm/contest/vip-index'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
}

class CowSpider:
    # 找到且解析所有考试
    def find_analysis_exams(self):
        exam_info_exam_list = self.tree.xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div')
        # print(exam_info_exam_list)
        exam_edinfo_list = []
        ok = True
        for exam in exam_info_exam_list:
            if ok:
                ok = False
                continue

            exam_list = {}

            # 考试名
            exam_name = exam.xpath('.//div[2]/div[1]/h4/a/text()')[0]
            exam_list['name'] = exam_name
            # print(exam_name)

            #考试时间
            exam_time = exam.xpath('./div[2]/div[1]/ul/li[2]/text()')[0]
            t = exam_time.split('\n')
            exam_edtime = ""
            for i in t:
                exam_edtime += i
            
            t1 = exam_edtime.split("比赛时间：    ")[1]
            t2 = t1.split(" (")[0]
            exam_edtime = t2.split("     ")[0] + ' ' + t2.split("     ")[1]
            exam_list['time'] = exam_edtime
            # print(exam_edtime)

            #url
            exam_url = "https://ac.nowcoder.com" + exam.xpath('.//div[2]/div[1]/h4/a/@href')[0]
            exam_list['url'] = exam_url
            # print(exam_url)

            # print(exam_list)
            exam_edinfo_list.append(exam_list)

        return exam_edinfo_list

    def main(self):
        # 获取页面源码
        response = requests.get(url=url, headers=headers)
        page_text = response.text

        self.tree = etree.HTML(page_text)

        # 找到且解析所有考试，并返回所有考试信息列表
        exam_info_list = self.find_analysis_exams()

        # print(exam_info_list)
        
        return exam_info_list


if __name__ == '__main__':
    spider = CowSpider()
    spider.main()