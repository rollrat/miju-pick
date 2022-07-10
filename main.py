from time import time
import requests
from bs4 import BeautifulSoup
import time

file = open("./result.txt", "a", encoding='utf8')

i = 0

for i in range(1, 5000):
    URL = 'https://gall.dcinside.com/mgallery/board/lists/?id=stockus&page=%d' % i
    res = requests.get(URL,  headers={
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'})
    soup = BeautifulSoup(res.text, 'html.parser')
    gg = soup.select('table.gall_list tr.ub-content')

    for tit in gg:
        s = '[' + tit.select('td.gall_num')[0].text + '] ' + \
            tit.select('td.gall_tit')[0].findChild().text
        file.write(s + '\n')
        file.flush()

    i += 1

    if i % 50 == 0:
        time.sleep(10)

    print(i)
