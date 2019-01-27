import requests
from bs4 import BeautifulSoup
import datetime
import config_para

url = config_para.url


def get_timestamp():# 获得现在时间的时间戳，如：20190125
    now_time = datetime.datetime.now()
    return(str(now_time)[0:4] + str(now_time)[5:7] + str(now_time)[8:10])

def get_weather(day_num = 3):
    moji_html = requests.get(url)
    moji_html.encoding = 'utf-8'# 获取墨迹天气的html并用utf-8解码
    soup = BeautifulSoup(moji_html.content, features="html.parser")# 解析成soup
    weather_part = soup.find_all("div", class_="detail_future_grid")# 找到和天气有关的part
    weather_part = BeautifulSoup(str(weather_part), features="html.parser")# 将其也解析成soup

    wea = weather_part.find_all(class_="wea")# 将天气状况提取出来
    wea_string = []
    for elements in wea:
        wea_string.append(elements.string)

    week = weather_part.find_all(class_="week")# 同理分别提取日期、温度
    week_string = []
    for elements in week:
        week_string.append(elements.string)

    temp_low = weather_part.find_all("strong")
    temp_low_string = []
    for elements in temp_low:
        temp_low_string.append(elements.string)

    temp_high = weather_part.find_all("b")
    temp_high_string = []
    for elements in temp_high:
        temp_high_string.append(elements.string)

    weather_info = {}# 将其整合至一个字典中
    for i in range(day_num + 1):
        year = get_timestamp()[0:4]
        id = str(year) + str(week_string[2 * i + 1])[0:2] + str(week_string[2 * i + 1])[3:5]
        weather_info[id] = [week_string[2 * i], week_string[2 * i + 1], wea_string[i], wea_string[i + 1], temp_low_string[i], temp_high_string[i]]

    weather_info.pop(str(int(get_timestamp()) - 1))

    return weather_info

if __name__ == '__main__':
    print(get_weather())
    weather_info = get_weather()


