import requests
from lxml import etree
url = 'https://atcoder.jp/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',

}

class AtCoderSpider:
    # 找到且解析所有考试
    def find_analysis_exams(self):
        exam_info_list = self.tree.xpath('//*[@id="contest-table-upcoming"]/div/table/tbody/tr')
        
        exam_edlist = []
        for exam in exam_info_list:
            exam_list = {}
            # 考试时间
            exam_time = exam.xpath('./td[1]//time/text()')[0]
            exam_time = str(exam_time).split("+0900")[0] # 去掉时区
            exam_list['time'] = exam_time

            # 考试名字
            exam_name = ""
            exam_name_list = exam.xpath('./td[2]//text()')
            t2 = ""

            if "（" in exam_name_list[3] or "）" in exam_name_list[3]:
                t1 = exam_name_list[3].split('（')[1]
                t2 = t1.split("）")[0]
            else: t2 = exam_name_list[3]

            for i in range(2):
                exam_name += exam_name_list[i]
            exam_list['name'] = exam_name + t2

            # print(exam_name)

            # url
            exam_url = "https://atcoder.jp" + exam.xpath('./td[2]/small/a/@href')[0]

            exam_list['url'] = exam_url

            exam_edlist.append(exam_list)
            
        return exam_edlist

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
    spider = AtCoderSpider()
    spider.main()


