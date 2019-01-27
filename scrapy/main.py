import requests
from bs4 import BeautifulSoup
import re
import config_para

def get_province():
    country = config_para.country
    city_index_url = "https://tianqi.moji.com/forecast7/%s" % country
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

def get_location_url(city_index_url):
    city_index_html = requests.get(city_index_url)
    city_index_html.encoding = "utf-8"
    soup = BeautifulSoup(city_index_html.content, features="html.parser")
    pattern = re.compile('[\u4e00-\u9fa5].{1,4}市$')
    city_a = soup.find_all("a", text=pattern)
    print(city_a)

get_location_url('https://tianqi.moji.com/forecast7/china/anhui')






# city_index_url = 'https://tianqi.moji.com/forecast7/china/anhui'
# city_index_html = requests.get(city_index_url)
# city_index_html.encoding = "utf-8"
# soup = BeautifulSoup(city_index_html.content, features="html.parser")
# city = soup.find_all(class_="city_hot")
# soup = BeautifulSoup(str(city), features="html.parser")
# city = soup.find_all("a")
# city_name = []
# for i in city:
#     city_name.append(i.string)
#
# pattern = re.compile('[\u4e00-\u9fa5].{1,4}市')
# result = pattern.findall(str(city_name))
# print(result)
# print(soup.find_all("a", text=pattern))
#


