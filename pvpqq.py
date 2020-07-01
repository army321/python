import requests
import time

star_time = time.time()
# url
base_url = "https://pvp.qq.com/web201605/js/herolist.json"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
}

# 请求数据

response = requests.get(url=base_url, headers=headers)
data_list = response.json()
# print(data_list) # gbk 编码 这个显示读取的json内容，是所有英雄的字典

for data in data_list:
    #   print(data)
    cname = data["cname"]
    ename = data["ename"]
    try:
        skin_name = data["skin_name"].split("|")
    except:
        pass
    # print(cname, ename, skin_name)

    for skin_num in range(1, len(skin_name) + 1):
        # background: url("//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/507/507-bigskin-2.jpg") center 0px;
        skin_url = (
            r"http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/"
            + str(ename)
            + "/"
            + str(ename)
            + "-bigskin-"
            + str(skin_num)
            + ".jpg"
        )
        # print(skin_url)
        time.sleep(0.5)
        skin_data = requests.get(url=skin_url, headers=headers).content
        with open(
            "img\\" + cname + "-" + skin_name[skin_num - 1] + ".jpg", mode="wb"
        ) as f:
            print("当前下载: " + cname + "-" + skin_name[skin_num - 1] + ".jpg")
            f.write(skin_data)

end_time = time.time()
print('下载时间：' + str(end_time-star_time))