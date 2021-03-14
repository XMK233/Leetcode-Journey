import requests
from lxml import html
import tqdm, time, requests, json
from lxml import etree
from selenium import webdriver
# from fake_useragent import UserAgent
import random, time, re, os

alreadyDownloaded = [fn.replace(".py", "") for fn in os.listdir(os.getcwd())]

## 初始化浏览器
chromeOptions = webdriver.ChromeOptions()
# chromeOptions.add_argument('--headless')  # use headless mode
driverSource = webdriver.Chrome(executable_path=r"C:\Users\XMK23\Downloads\chromedriver.exe",
                          chrome_options=chromeOptions)
# driver = webdriver.Chrome(executable_path=r"C:\Users\XMK23\Downloads\chromedriver.exe",
#                           chrome_options=chromeOptions)

driverSource.get("https://www.nowcoder.com/company/home/code/665?codeType=1")   #"https://leetcode-cn.com/problemset/lcof/#page-{}".format(pageNum))
time.sleep(2)

## 爬虫加载的时间
loadTime = 10
## 首先是按页码，一页一页来。
while True:
    # try:
    rendered_body = driverSource.page_source
    page_source = etree.HTML(rendered_body)
    ## 获取一页上所有的url
    # titles = [s.split()[-1] for s in page_source.xpath('//td[@value="[object Object]"][2]/text()')]
    # urls = page_source.xpath('//div[@class="question-title"]/a/@href')
    ids = page_source.xpath("//td[@class='offer-pot']/text()")
    titles = page_source.xpath("//td[@class='txt-left']/span/text()")
    difficulties = page_source.xpath("//td[@style='text-align: left;']/text()")
    urls = page_source.xpath("//tr[@data-href]/@data-href")
    ## 逐个url进行处理。
    counter = 0
    for id, title, difficulty, url in tqdm.tqdm(zip(ids, titles, difficulties, urls)):
        fullUrl = "https://www.nowcoder.com" + url

        # driver.get(fullUrl)
        # time.sleep(3)
        # rendered_body = driver.page_source
        # page_source = etree.HTML(rendered_body)
        # texts = page_source.xpath('//div[@class="notranslate"]//text()')
        # texts_total = "".join(texts).replace(u'\xa0', u' ')
        # heheda = driver.find_element_by_xpath("//div[@class='notranslate']")

        ## 要等一下ho, 等他加载ho.
        ## 如果有加载失败的, 可以再调高这个等待的时间.
        # time.sleep(10)
        ## 打印信息到文件里。
        # try:
        pyFileName = "{}-{}-{}".format(id.strip(), title.strip(), difficulty)
        if pyFileName in alreadyDownloaded:
            continue
        with open(pyFileName + ".py", "w", encoding="utf-8") as f:
            f.write("# -*- coding:utf-8 -*-\n'''\n{}\n\n\n'''\n".format(fullUrl))
        # except:
        #     pass
        # break

    button = driverSource.find_element_by_xpath("//button[@class='btn-next']")
    try:
        button_failed = driverSource.find_element_by_xpath("//button[@class='btn-next' and @disabled]")
        break
    except:
        button.click()
        time.sleep(2)

    # except:
    #     break


## 最后会崩掉，但是没事的。
driverSource.close()
# driver.close()