import requests
from bs4 import BeautifulSoup
import get_weather
import configparser

conf = configparser.ConfigParser()
conf.read_file(open('config_para.ini'))
location = conf.get("location", "location")

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

def main(location = location):# 将信息整合成一个字典的形式
    uray = conf.get("url", "uray")
    makeup = conf.get("url", "makeup")
    pollution = conf.get("url", "pollution")
    try:
        uray_url = eval(uray) + eval(location)
        makeup_url = eval(makeup) + eval(location)
        pollution_url = eval(pollution) + eval(location)
    except:
        uray_url = eval(uray) + location
        makeup_url = eval(makeup) + location
        pollution_url = eval(pollution) + location
    url = [uray_url, makeup_url, pollution_url]
    id = [get_timestamp, str(int(get_timestamp) + 1), str(int(get_timestamp) + 2)]
    living_info = {}
    uray_info = get_content(url[0])
    makeup_info = get_content(url[1])
    pollution_info = get_content(url[2])
    for i in range(3):
        living_info[id[i]] = [uray_info[2*i:2*i+2], makeup_info[2*i:2*i+2], pollution_info[2*i:2*i+2]]
    print("get_living_index success!")
    return living_info

if __name__ == '__main__':
    print(main())
    living_info = main()





