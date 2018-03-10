import urllib.request

def get(url):
    url = url or "https://www.baidu.com/"
    fp = urllib.request.urlopen(url)
    html_byte = fp.read()
    html_str = html_byte.decode('utf8')
    fp.close()
    return html_str

