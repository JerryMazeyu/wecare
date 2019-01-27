import requests
from bs4 import BeautifulSoup
import config_para
import get_weather

url = [config_para.uray, config_para.makeup, config_para.pollution]# 将url定义为配置文件中的url

def get_content(url):# 从指定url（紫外线、化妆、污染）中获取指标和建议
    moji_html = requests.get(url)
    moji_html.encoding = "utf-8"
    soup = BeautifulSoup(moji_html.content, features="html.parser")
    living_part_1 = soup.find_all("dd", class_="aqi_desc")
    living_part_2 = soup.find_all("div", class_="aqi_forecast_hid")
    text = []
    for i in range(len(living_part_1)):
        text.append(living_part_1[i].span.string)
        text.append(living_part_2[i].p.string)
    return text

get_timestamp = get_weather.get_timestamp()# 引用get_weather脚本中获取时间戳的函数

def main():# 将信息整合成一个字典的形式
    id = [get_timestamp, str(int(get_timestamp) + 1), str(int(get_timestamp) + 2)]
    living_info = {}
    uray_info = get_content(url[0])
    makeup_info = get_content(url[1])
    pollution_info = get_content(url[2])
    for i in range(3):
        living_info[id[i]] = [uray_info[2*i:2*i+2], makeup_info[2*i:2*i+2], pollution_info[2*i:2*i+2]]
    return living_info

if __name__ == '__main__':
    print(main())
    living_info = main()





