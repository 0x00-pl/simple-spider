import time
import get_small_page

def get_list(url_list, interval):
    interval = interval or 10
    ret = []
    for url in url_list:
        html = get_small_page(url)
        ret.append(html)
        time.sleep(interval)

    return ret

