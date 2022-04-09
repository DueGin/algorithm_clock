import requests
from lxml import etree
url = 'https://codeforces.com/contests?complete=true'
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
}

dd = {'Jan' : '01', 'Feb' : '02', 'Mar' : '03', 'Apr' : '04', 'May' : '05', 'Jun' : '06', 'Jul' : '07', 'Aug' : '08', 'Sept' : '09', 'Oct' : '10', 'Nov' : '11', 'Dec' : '12'}

class CF_Spider:
    def __init__(self):
        pass

    def get_exam(self):
        exam_info_list = self.tree.xpath('//*[@id="pageContent"]/div[1]/div[1]/div[6]/table//tr')

        exam_list = []
        skip = True
        for exam_info in exam_info_list:
            if skip:
                skip = False
                continue

            exam = {}
            #id
            id = exam_info.xpath('./@data-contestid')[0]
            exam['id'] = id
            # print(id)

            #url
            url = 'https://codeforces.com/contests/' + id
            exam['url'] = url

            #考试名
            name = exam_info.xpath('./td[1]/text()')[0]
            name = name.split("\r\n")[1]
            if '(' in name or ')' in name:
                if 'Div' not in name:
                    name = name.split('(')[0]

            exam['name'] = name
            # print(name)

            #时间
            time = exam_info.xpath('./td[3]/a//text()')[1]
            ll = time.split('/')
            month = ll[0]
            day = ll[1]
            year = ll[2].split()[0]
            tt = ll[2].split()[1]
            date = year + '-' + dd[month] + '-' + day + ' ' + tt
            # print(date)
            exam['time'] = date

            exam_list.append(exam)

        return exam_list

    def main(self):
        # 获取页面源码
        response = requests.get(url=url, headers=headers)

        page_text = response.text
        # print(page_text)

        self.tree = etree.HTML(page_text)

        exam_data = self.get_exam()
        # print(exam_data)
        return exam_data

if __name__ == '__main__':
    spider = CF_Spider()
    spider.main()