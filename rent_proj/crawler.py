import csv
from concurrent.futures import ThreadPoolExecutor

import requests
from bs4 import BeautifulSoup


def get_url(page):
    print("fetch: ", url.format(page=page))
    response = requests.get(url.format(page=page))
    response.encoding = 'utf-8'
    return response.text


def down_csv(content):
    html = BeautifulSoup(content, 'lxml')
    house_list = html.select(".list > li")

    for house in house_list:
        house_title = house.select("h2")[0].string
        house_url = "http://bj.58.com/%s" % (house.select("a")[0]["href"])
        house_info_list = house_title.split()

        # 如果第二列是公寓名则取第一列作为地址
        if "公寓" in house_info_list[1] or "青年社区" in house_info_list[1]:
            house_location = house_info_list[0]
        else:
            house_location = house_info_list[1]

        house_money = house.select(".money")[0].select("b")[0].string
        with open("rent.csv", "a", encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(
                [house_title, house_location, house_money, house_url])


if __name__ == '__main__':
    url = "http://bj.58.com/pinpaigongyu/pn/{page}/?minprice=2000_4000"
    # 已完成的页数序号，初时为0
    page = 0
    tpool = ThreadPoolExecutor(max_workers=5)
    for i in range(1, 76):
        tpool.submit(get_url, i).add_done_callback(down_csv)
