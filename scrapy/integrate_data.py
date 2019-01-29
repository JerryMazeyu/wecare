import get_living_index
import get_weather
import configparser

conf = configparser.ConfigParser()
conf.read_file(open('config_para.ini'))
location = conf.get("location", "location")

def integrate_data(location = location):# 整合数据
    weather_info = get_weather.get_weather(location)
    living_info = get_living_index.main(location)
    final_info = {}
    for key in weather_info:
        if living_info.get(key):
            final_info[key] = [weather_info[key], living_info[key]]
        else:
            final_info[key] = weather_info[key]
    for key in living_info:
        if weather_info.get(key):
            pass
        else:
            final_info[key] = living_info[key]
    print("intergrate_data success!")
    return final_info

if __name__ == '__main__':
    print(integrate_data("china/anhui/bengbu"))