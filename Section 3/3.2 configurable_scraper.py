#!/bin/python
"""
configurable_scraper.py

Purpose: User configurable web scraper

Author: Cody Jackson

Date: 2/18/2018
########################
Version 0.1
    Initial build
"""
from collections import namedtuple
from random import randrange
import requests

http_proxies = ["183.82.116.56:8080", "217.13.102.86:3128", "218.255.102.246:8060"]
user_agents = ["Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 "
               "Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"]


def random_agent():
    """Randomize the user-agent provided to the server."""
    agent_index = randrange(0, len(user_agents))
    headers = {"user-agent": "{}".format(user_agents[agent_index])}

    return headers


def random_proxy():
    """Randomize the proxy service that provides the user IP to the server."""
    proxy_index = randrange(0, len(http_proxies))
    proxy = {"http": "{}".format(http_proxies[proxy_index])}

    return proxy


def scraper_request():
    """Pull HTML and cookies from target."""
    r = requests.get("http://testing-ground.scraping.pro/whoami", proxies=random_proxy(), headers=random_agent())

    return r.text, r.cookies


if __name__ == "__main__":
    scrape_results = scraper_request()

    Scraper = namedtuple("Scraper", ["html", "cookies"])
    scrape = Scraper(scrape_results[0], scrape_results[1])

    print(scrape.html)
    print(scrape.cookies)
