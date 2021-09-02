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
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
}

headersx = {
'Accept': "application/json, text/javascript, */*; q=0.01",
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'Connection': 'keep-alive',
'Content-Length': '599',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': '',
'DNT': '1',
'Host': 'pdc.njucm.edu.cn',
'Origin': 'https://pdc.njucm.edu.cn',
'Referer': 'https://pdc.njucm.edu.cn/pdc/formDesignApi/S/iKKUJvEV',
'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
'sec-ch-ua-mobile': '?0',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'
}

params = {
'DATETIME_CYCLE': '',
'DLM_455532': '',
'XM_699791': '',
'RADIO_816586': '境内',
'PICKER_894219': '',
'TEXT_362765': '',
'RADIO_773105': '健康',
'RADIO_252419': '否',
'SELECT_502461': '',
'SELECT_96317': '36.7℃及以下',
'RADIO_223980': '否',
'SELECT_117762': '',
'SELECT_631415': '36.8℃',
'RADIO_944199': '否',
'TEXT_625091': '',
'RADIO_655596': '否',
'TEXTAREA_901197': '无',
'CHECKBOX_712638': '同意并承诺'
}
cookie = os.environ["COOKIE"]
name = os.environ["NAME"]
student_number = os.environ["STUDENT_NUMBER"]
location = os.environ["LOCATION"]

params['DLM_455532'] = student_number
params['XM_699791'] = name
params['PICKER_894219'] = location

headers['Cookie'] = cookie
headersx['Cookie'] = cookie

now_time = datetime.datetime.now().strftime('%Y/%m/%d')
params['DATETIME_CYCLE'] = now_time
print(params['DATETIME_CYCLE'] )
res = requests.get('https://pdc.njucm.edu.cn/pdc/formDesignApi/S/iKKUJvEV',headers=headers)
if res.status_code == 200:
    if res.text.find('提交'):
        print('Cookie Check Pass')
        res = requests.post('https://pdc.njucm.edu.cn/pdc/formDesignApi/dataFormSave?wid=A25FF315167F5528E0533200140AA058&userId=584820247',data=params,headers=headersx)
        if res.status_code == 200:
            print('Date Success Post')
        else:
            print('Error' + res.status_code)
    
