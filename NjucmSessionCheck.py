import requests
import datetime
import os

headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': '',
'DNT': '1',
'Host': 'pdc.njucm.edu.cn',
'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
'sec-ch-ua-mobile': '?0',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4585.179 Safari/547.36',
}

cookie = os.environ["COOKIE"]
headers['Cookie'] = cookie

now_time = datetime.datetime.now().strftime('%Y/%m/%d')
print(now_time)
res = requests.get('https://pdc.njucm.edu.cn/pdc/formDesignApi/S/iKKUJvEV',headers=headers)
if res.status_code == 200:
    if res.text.find('提交'):
        print('Cookie Check Pass')
    else:
        print('Error' + res.status_code)
