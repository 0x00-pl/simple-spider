import urllib.request
import urllib.parse
import requests

def get(url):
    url = url or "https://www.baidu.com/"
    fp = urllib.request.urlopen(url)
    html_byte = fp.read()
    html_str = html_byte.decode('utf8', 'ignore')
    fp.close()
    return html_str

def post(url, post_data=None):
    url = url or "https://www.baidu.com/"
    post_data = post_data or {}
    response = requests.post(url, data=post_data)
    html_str = response.text
    return html_str
