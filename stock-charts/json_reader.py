import csv
import json
import datetime

data_list = []
name_list = ['人民币', '长江传媒', '广电网络', '中文传媒', '时代出版', '春兰股份', '厦华电子', '惠而浦', '澳柯玛', '均胜电子', '曙光股份', '易见股份', '海正药业', '中恒集团', '复星医药', '江苏吴中', '大唐电信', '大恒科技', '信威集团', '康欣新材']
with open('./action.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    current_time = datetime.date(2018, 1, 1)
    time_step = datetime.timedelta(days=1)
    for row in reader:
        time_str = str(current_time.strftime('%Y-%m-%d'))
        item = {'xList': name_list, 'yList': row, 'date': time_str}
        data_list.append(item)
        current_time = current_time + time_step
with open('./json.json', 'w', newline='') as jsonFile:
    dump_dict = {'dataList': data_list}
    json_string = json.dumps(dump_dict, indent= 4)
    jsonFile.write(json_string)
print('保存完毕！')
