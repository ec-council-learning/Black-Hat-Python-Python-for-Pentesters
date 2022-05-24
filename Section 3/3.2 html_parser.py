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
from bs4 import BeautifulSoup


if __name__ == "__main__":
    # file cannot have an extension
    with open("table_report") as html_file:
        soup = BeautifulSoup(html_file, "lxml")

    print(soup.title)
    print(soup.title.string)
    for cell in soup.find_all("td"):
        print(cell)
    print(soup.prettify())
    print(soup.get_text())
