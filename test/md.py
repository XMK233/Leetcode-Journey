import hashlib, time
import urllib.request
import sys
import re, requests, time
from lxml import etree

typ = sys.getfilesystemencoding()


def translate1(querystr, to_l="zh", from_l="en"):  # "en", "fr", "auto"
    '''for google tranlate by doom
    '''
    t = list(querystr)
    for i in range(0, len(t)):
        if ord(t[i]) > 127:
            t[i] = "+"
    querystr = ''.join(t)
    # print(querystr)
    C_agent = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.165063 Safari/537.36 AppEngine-Google."}
    flag = 'class="t0">'
    tarurl = "https://translate.google.com/?source=gtx_c#view=home&op=translate&sl=zh-CN&tl=en&text={}".format(
        querystr.replace(" ",
                         "+"))  # "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (to_l, from_l, querystr.replace(" ", "+"))

    request = urllib.request.Request(tarurl, headers=C_agent)
    page = str(urllib.request.urlopen(request).read().decode(typ))
    target = page[page.find(flag) + len(flag):]
    target = target.split("<")[0]
    return target


def translate(querystr, to_l="zh", from_l="en"):  # "en", "fr", "auto"
    '''for google tranlate by doom
    '''
    t = list(querystr)
    for i in range(0, len(t)):
        if ord(t[i]) > 127:
            t[i] = "+"
    querystr = ''.join(t)
    # print(querystr)
    C_agent = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.165063 Safari/537.36 AppEngine-Google."}
    flag = 'class="t0">'
    tarurl = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (
    to_l, from_l, querystr.replace(" ", "+"))  # http://translate.google.com/m?hl=zh&sl=en&q=Summary.
    # print(tarurl)
    data = requests.get(tarurl, headers=C_agent)
    time.sleep(0.1)  ##
    response = etree.HTML(data.text)
    # print(data.text)
    result1 = response.xpath("//div[@class='result-container']/text()")
    result2 = response.xpath("//div[@dir]/text()")
    if len(result1) > 0:
        return result1[0]
    if len(result2) > 0:
        return result2[0]
    # return result1 or result2


k = 0

f1 = open("source.pts", encoding='UTF-8')
f = hashlib.md5()
f.update("".join(f1.readlines()).encode("utf-8"))
t0 = f.hexdigest()
f1.close()
print("let's go")
while True:
    # print("this is a turn %d" %(k))
    k += 1
    f1 = open("source.pts", encoding='UTF-8')
    f = hashlib.md5()
    f.update("".join(f1.readlines()).encode("utf-8"))
    t1 = f.hexdigest()
    f1.close()

    if t1 == t0:
        pass
    else:
        t0 = t1
        o = open("target.pts", "w", encoding="utf-8")
        s = ""
        t = open("source.pts", encoding='UTF-8')
        while 1:
            line = t.readline()
            if not line:
                break
            s += line.replace("\n", " ")

        ###########
        s = s.replace("et al.", "et al+").replace("etc.", "etc+").replace("e.g.", "e+g+").replace("i.e.",
                                                                                                  "i+e+").replace(
            "U.S.", "U+S+").replace("Ph.D.", "PhD")

        decimals = re.findall("(\d+\.\d+)", s)
        for _ in decimals:
            decimal = _.replace(".", ",")
            s = s.replace(_, decimal)
        s = s.strip()  # delete blank characters.
        # print(s)
        # print(s)

        ########## Edition 1
        for sen in re.split("\.|\?", s):
            sen = sen.strip()
            # print(sen)
            if sen != "":
                o.write(sen + "." + "\n")
                # print(sen + ".")
                o.write(translate(sen + ".") + "\n" + "\n")

        o.close()
        t.close()

    time.sleep(2)

# print (md5.new(f1.read()).digest() == md5.new(f2.read()).digest())