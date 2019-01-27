#参数设置（以后写在ini文件里面）
country = "china"
province = "shanghai"
city = "shanghai"
location = "%s/%s/%s" % (country, province, city)
url = "https://tianqi.moji.com/forecast7/%s" % location# 预测的url

uray = "https://tianqi.moji.com/uray/%s/%s/%s" % (country, province, city)# 生活指数的相关url，分别是紫外线、化妆指数、污染指数
makeup = "https://tianqi.moji.com/makeup/%s/%s/%s" % (country, province, city)
pollution = "https://tianqi.moji.com/pollution/%s/%s/%s" % (country, province, city)