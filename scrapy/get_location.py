import requests
from bs4 import BeautifulSoup
import re
import configparser

def get_province():
    conf = configparser.ConfigParser()
    conf.read_file(open('config_para.ini'))
    country = conf.get("location", "country")
    forecast = conf.get("url", "forecast")
    city_index_url = eval(forecast) + eval(country)
    city_index_html = requests.get(city_index_url)
    city_index_html.encoding = "utf-8"
    soup = BeautifulSoup(city_index_html.content, features="html.parser")
    province = soup.find_all(class_="city_list clearfix")
    province_url = []
    province_name = []
    for i in province:
        province_name.append(i.a.string)
        province_url.append("https://tianqi.moji.com" + i.a["href"])
    return province_name, province_url

def get_location_id(city_index_url):
    city_index_html = requests.get(city_index_url)
    city_index_html.encoding = "utf-8"
    soup = BeautifulSoup(city_index_html.content, features="html.parser")
    pattern = re.compile('[\u4e00-\u9fa5].{1,4}市$')
    city_a = soup.find_all("a", text=pattern)
    location = []
    pattern_1 = re.compile('china/.*"')
    for i in city_a:
        location_p = pattern_1.findall(str(i))
        location.append(location_p[0][:-1])
    return location

def get_all_location():
    urls = get_province()[1]
    locations = []
    for url in urls:
        temp = get_location_id(url)
        locations = locations + temp
    print("get_all_location success!")
    return locations

if __name__ == '__main__':
    print(type(get_all_location()))