import get_living_index
import get_weather

weather_info = get_weather.get_weather()
living_info = get_living_index.main()
final_info = {}

def integrate_data():# 整合数据
    weather_info = get_weather.get_weather()
    living_info = get_living_index.main()
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
    return final_info


