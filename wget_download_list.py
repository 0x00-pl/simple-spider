import os
import time

def download_once(url):
    cmd = 'wget ' + url
    os.system(cmd)

def download_list(url_list, interval):
    for url in url_list:
       download_once(url)
       time.sleep(interval)
