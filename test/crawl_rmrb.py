import requests
import bs4
import os
import datetime
import time


def fetchUrl(url):
    '''
    功能：访问 url 的网页，获取网页内容并返回
    参数：目标网页的 url
    返回：目标网页的 html 内容
    '''

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }

    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text


def getPageList(year, month, day):
    '''
    功能：获取当天报纸的各版面的链接列表
    参数：年，月，日
    '''
    url = 'http://www.81.cn/jfjbmap/content/{}-{}/{}/node_2.htm'.format(year, month, day)
    # url = 'http://paper.people.com.cn/rmrb/html/' + year + '-' + month + '/' + day + '/nbs.D110000renmrb_01.htm'
    html = fetchUrl(url)
    bsobj = bs4.BeautifulSoup(html, 'html.parser')
    pageList = bsobj.find('div', attrs={'class': 'col-md-4-10 channel-list'}).ul.find_all('li')# , attrs={'class': 'right_title-name'}
    linkList = []

    for page in pageList:
        link = page.a["href"]
        url = url = 'http://www.81.cn/jfjbmap/content/{}-{}/{}/{}'.format(year, month, day, link.replace("./", "")) # 'http://paper.people.com.cn/rmrb/html/' + year + '-' + month + '/' + day + '/' + link
        linkList.append(url)

    return linkList


def getTitleList(year, month, day, pageUrl):
    '''
    功能：获取报纸某一版面的文章链接列表
    参数：年，月，日，该版面的链接
    '''
    html = fetchUrl(pageUrl)
    bsobj = bs4.BeautifulSoup(html, 'html.parser')
    titleList = bsobj.find('div', attrs={'class': 'newslist-item current'}).ul.find_all('li')
    linkList = []

    for title in titleList:
        tempList = title.find_all('a')
        for temp in tempList:
            link = temp["href"]
            url = 'http://81.cn/jfjbmap/content/' + year + '-' + month + '/' + day + '/' + link
            linkList.append(url)
            # if 'nw.D110000renmrb' in link:
            #     url = 'http://paper.people.com.cn/rmrb/html/' + year + '-' + month + '/' + day + '/' + link
            #     linkList.append(url)

    return linkList


def getContent(html):
    '''
    功能：解析 HTML 网页，获取新闻的文章内容
    参数：html 网页内容
    '''
    bsobj = bs4.BeautifulSoup(html, 'html.parser')

    # 获取文章 标题
    title = bsobj.h2.text + '\n' # bsobj.h3.text + '\n' + bsobj.h1.text + '\n' + bsobj.h2.text + '\n'
    # print(title)

    # 获取文章 内容
    pList = bsobj.find('div', attrs={'id': 'APP-Content'}).find_all('p')
    content = ''
    for p in pList:
        content += p.text + '\n'
        # print(content)

    # 返回结果 标题+内容
    resp = title + content
    return resp


def saveFile(content, path, filename):
    '''
    功能：将文章内容 content 保存到本地文件中
    参数：要保存的内容，路径，文件名
    '''
    # 如果没有该文件夹，则自动生成
    if not os.path.exists(path):
        os.makedirs(path)

    # 保存文件
    with open(os.path.join(path, filename), 'w', encoding='utf-8') as f:
        f.write(content)


def download_rmrb(year, month, day, destdir):
    '''
    功能：爬取《人民日报》网站 某年 某月 某日 的新闻内容，并保存在 指定目录下
    参数：年，月，日，文件保存的根目录
    '''
    pageList = getPageList(year, month, day)
    for page in pageList:
        titleList = getTitleList(year, month, day, page)
        for url in titleList:
            # 获取新闻文章内容
            html = fetchUrl(url)
            content = getContent(html)

            # 生成保存的文件路径及文件名
            # temp = url.split('_')[2].split('.')[0].split('-')
            pageNo = pageList.index(page) + 1 # temp[1]
            _ = titleList.index(url) + 1
            titleNo = str(_) if _ > 10 else "0" + str(_) # temp[0] if int(temp[0]) >= 10 else '0' + temp[0]
            path = os.path.join(destdir, year + month + day)# destdir + '/' + year + month + day + '/'
            # fileName = year + month + day + '-' + pageNo + '-' + titleNo + '.txt'
            fileName = "{}{}{}-{}-{}.txt".format(year, month, day, pageNo, titleNo)
            # 保存文件
            saveFile(content, path, fileName)

def gen_dates(b_date, days):
    day = datetime.timedelta(days = 1)
    for i in range(days):
        yield b_date + day * i
def get_date_list(beginDate, endDate):
    start = datetime.datetime.strptime(beginDate, "%Y%m%d")
    end = datetime.datetime.strptime(endDate, "%Y%m%d")
    data = []
    for d in gen_dates(start, (end-start).days):
        data.append(d)
    return data
if __name__ == '__main__':
    beginDate = "20190506"# input('请输入开始日期:')
    endDate = "20190507"# input('请输入结束日期:')
    data = get_date_list(beginDate, endDate)
    for d in data:
        year = str(d.year)
        month = str(d.month) if d.month >=10 else '0' + str(d.month)
        day = str(d.day) if d.day >=10 else '0' + str(d.day)
        download_rmrb(year, month, day, 'data')
        print("爬取完成：" + year + month + day)

# if __name__ == '__main__':
#     '''
#     主函数：程序入口
#     '''
#     year = "2019"
#     month = "05"
#     day = "06"
#     destdir = os.getcwd()
#
#     download_rmrb(year, month, day, destdir)
#     print("爬取完成：" + year + month + day)