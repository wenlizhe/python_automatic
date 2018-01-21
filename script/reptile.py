# -*- coding: utf-8 -*-
import webbrowser
import requests
import bs4
import logging
import os
# import urllib3.contrib.pyopenssl 
# urllib3.contrib.pyopenssl.inject_into_urllib3()
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# import urllib3.util.ssl_
# urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'


def test():
    pass
    # webbrowser.open('https://www.baidu.com')
    # re = requests.get('http://www.gamersky.com/', verify=True)
    # re = open('../test_dir/example.html', encoding="utf-8")
    # re.raise_for_status()

    # soup = bs4.BeautifulSoup(re, "html5lib")
    # print(soup)
    # elems = soup.select('#noscript-warning')
    # logging.debug(elems)
    # print(elems[0].getText())
    # print(elems[0].getText())
    # playfile = open('RomeoAndJuliet.txt', 'wb')
    # for chunk in re.iter_content(100000):
    #     playfile.write(chunk)

    # playfile.close()


def download_pic():
    url = 'https://xkcd.com'
    os.makedirs('../test_dir/xkcd', exist_ok=True)
    while not url.endswith('#'):
        # TODO:Download page
        print('Download page %s...' % url)
        re = requests.get(url, verify=False)
        re.raise_for_status()

        soup = bs4.BeautifulSoup(re.text, "html5lib")

        # TODO:find pic url
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            # download pic
            print('download image %s...' % (comicUrl))
            re = requests.get(comicUrl)
            re.raise_for_status()

            # TODO:save image tp dir
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in re.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

        # get prev button`s url
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'https://xkcd.com' + prevLink.get('href')
    
    print('done')


if __name__ == '__main__':
    download_pic()
