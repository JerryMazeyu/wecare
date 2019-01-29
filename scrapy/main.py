import get_location
import get_weather
import json
import integrate_data

def main():
    timetstamp = get_weather.get_timestamp()
    filepath = "../weather_data/%s.json" % timetstamp
    locations = get_location.get_all_location()
    weather_info = {}
    for i in locations:
        print(i)
        temp = integrate_data.integrate_data(i)
        weather_info[i] = temp
    with open(filepath, "w") as f:
        json.dump(weather_info, f)
        print("成功写入！")

if __name__ == '__main__':
    main()

