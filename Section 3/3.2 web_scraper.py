#!/bin/python
"""
web_scraper.py

Purpose: Python-based web scraping tool that includes the ability to use proxy servers, change user-agent string, and
identify cookies from target server.

Author: Cody Jackson

Date: 2/17/2018
########################
Version 0.1
    Initial build
"""
import requests

proxies = {"http": "183.82.116.56:8080"}
headers = {"user-agent": "Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0"}

r = requests.get("http://testing-ground.scraping.pro/whoami", proxies=proxies, headers=headers)
print(r.text)
for cookie in r.cookies:
    print(cookie)
print(r.cookies["TestingGround"])
