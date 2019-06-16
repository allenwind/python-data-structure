import time
import argparse
import asyncio
import urllib.parse
import re

import aiohttp
import async_timeout
import fake_useragent

url_regexp = re.compile(r'^https?://\[?\w', re.IGNORECASE)
ua = fake_useragent.UserAgent(path=r'D:\database\headers.json')
root_urls = []
crawled_urls = set()

def generate_headers():
    return {'user-agent': ua.random}

async def get_body(url, timeout=10):
    async with aiohttp.ClientSession() as session:
        try:
            with async_timeout.timeout(timeout):
                headers = generate_headers()
                async with session.get(url, headers=headers) as response:
                    if response.status == 200:
                        html = await response.text()
                        return 200, html
                    else:
                        return response.status, None
        except Exception as err:
            return err, None

async def handle_task(task_id, queue):
    while not queue.empty():
        url = await queue.get()
        status, html = await get_body(url)
        crawled_urls.add(url)
        if html is None:
            print('error: %s url: %s' % (status, url))
        else:
            for url in get_urls(html):
                if url in crawled_urls:
                    continue
                else:
                    queue.put_nowait(url)

def parse_urls(html):
    return [remove_fragment(url) for url in url_regexp.findall(html)]

def get_urls(html):
    new_urls = [url.split('"')[0] for url in str(html).replace("'",'"').split('href="')[1:]]
    return [urljoin(root_url, remove_fragment(new_url)) for new_url in new_urls]

def remove_fragment(url):
    url, frag = urllib.parse.urldefrag(url)
    return url

def crawler(root_urls, task_size=10):
    queue = asyncio.Queue()
    for url in root_urls:
        queue.put_nowait(url)
    loop = asyncio.get_event_loop()
    tasks = [handle_task(task_id, queue) for task_id in range(task_size)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__ == '__main__':
    root_urls.append('https://www.baidu.com/')
    crawler(root_urls)

