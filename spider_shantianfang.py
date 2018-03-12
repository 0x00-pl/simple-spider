import re
import time
import get_page_list
import get_small_page
import wget_download_list
import urllib.request

def post(url):
    url = url or "https://www.baidu.com/"
    fp = urllib.request.urlopen(url)
    html_byte = fp.read()
    html_str = html_byte.decode('utf8', 'ignore')
    fp.close()
    return html_str


def get_index_page_list():
    base_url = ['http://www.shantianfang.com.cn/playdata/108/', '.html']
    ret = [str(i) for i in range(2, 320)]
    return [i.join(base_url) for i in ret]

def find_audio_urls(page_html):
    mp3_url_re = 'http://shantianfang11.shantianfang.com.cn/.*?\.flv'
    return re.findall(mp3_url_re, page_html)


def main(interval):
    index_list = get_index_page_list()
    mp3_urls_all = []
    for index_url in index_list:
        print('getting url:', index_url)
        page_html = get_small_page.post(index_url)
        mp3_urls = find_audio_urls(page_html)
        mp3_urls = [i.replace('.flv', '.mp3') for i in mp3_urls]
        print('\n'.join(mp3_urls))
        mp3_urls_all.extend(mp3_urls)
        time.sleep(interval)

    wget_download_list.download_list(mp3_urls_all, interval)
    return mp3_urls_all


if __name__ == '__main__':
    print(main(1))
