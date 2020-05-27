import requests
import parsel
import concurrent.futures

headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}


#封装函数，进行多线程操作

def send_request(url):
    response = requests.get(url=url,headers =headers,verify = False)
    return response

def parse_data(data):
    selector = parsel.Selector(data)
    result_list = selector.xpath('//a[@class="col-xs-6 col-sm-3"]')
    for result in result_list:
        img_url = result.xpath('./img/@data-original').extract_first()  #图片的url
        img_title = result.xpath('./img/@alt').extract_first()  #图片的标题

        #文件名称处理
        all_title = img_title+"."+img_url.split('.')[-1]

        yield all_title,img_url

def save_data(file_name,data):

    with open('img\\'+file_name,mode ='wb') as f:
        f.write(data)
        print('保存完成：' +file_name)

def main(page):
    num = 0
    for page in range(1,page +1):
        print('------当前正在读取{}-------'.format(page))
        thread_poll = concurrent.futures.ThreadPoolExecutor(max_workers=3)
        res = send_request('https://www.doutula.com/photo/list/?page={}'.format(page))
        src_url = parse_data(res.text)
        for file,url in src_url:
            num +=1
            print(num)
            image_response = send_request(url)
            thread_poll.submit(save_data,file,image_response.content)

        thread_poll.shutdown()


if __name__ == '__main__':
    main(5)
