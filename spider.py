import re
import requests

def getHTML(url):
    try:
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': 't=9885068bddd007f8897b9a7c0062bd9e; cookie2=1752f7fe28ef9b5093cde5a6192c1745; _tb_token_=ea9b378ee3aed; cna=ri46FKsulQMCAbfbibYJ4YfB; tg=0; thw=cn; alitrackid=www.taobao.com; hng=CN%7Czh-CN%7CCNY%7C156; enc=JWdlpKBInuxeAoWv73ws9f6Q9inqo83Tk5C%2Fj1JHBiDbQl61s34Bt5k2kvy9qUUpzYTqgJ8wszJnUUW0G2cgSw%3D%3D; l=Ao-P169FesrT543/u9DAGcuPnyiZ8uPH; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; lastalitrackid=www.taobao.com; ctoken=8g4bzPHVixtoJUZmonrxrhllor; _cc_=UIHiLt3xSw%3D%3D; mt=ci=0_0; v=0; JSESSIONID=8A6C51CECDD370813176747064304BA4; isg=BC0t-Tg_CkmrUe7XyGTqjGiiPMlnImBfMTvvLG8yaUQz5k2YN9pxLHu01Pql5nkU',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        }
        r = requests.get(url, headers = headers, timeout = 30)
        r.raise_for_status()
        return r.text
    except:
        return ""

def parseHTML(html, ilt):
    tlt = re.compile('"raw_title":"(.*?)"', re.S)
    plt = re.compile('"view_price":"(.*?)"', re.S)
    title = re.findall(tlt, html)
    price = re.findall(plt, html)
    for i in range(len(title)):
        ilt.append([price[i], title[i]])

def printList(ilt):
    tplt = "{0:4}\t{1:8}\t{2:}"
    print(tplt.format("序号", "价格", "商品名称"))
    for i in range(len(ilt)):
        print(tplt.format(i+1, ilt[i][0], ilt[i][1]))

def main():
    ilt = []
    depth = 3
    goods = '书包'
    for i in range(depth):
        url = 'https://s.taobao.com/search?q=%s&s=%s' %(goods,i*44)
        html = getHTML(url)
        parseHTML(html, ilt)
    printList(ilt)

main()