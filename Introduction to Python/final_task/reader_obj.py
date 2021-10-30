import argparse
import logging
import os
import sys
import json
import datetime
import xml.etree.ElementTree as ELTree
import requests as requests
from functools import lru_cache


def __date__(date):
    try:
        if len(date) < 8:
            raise ImportError("The date must be in the format %Y%m%d (20210219)")
    except ImportError as error:
        logger.error(error) if parser.args.verbose else print(error)
    return datetime.datetime.strptime(date, "%Y%m%d").strftime("%Y%m%d")


class Parser1:
    args = None
    root = str(os.path.dirname(sys.modules["__main__"].__file__))

    def __init__(self):
        # initialize the object, add the necessary parameters
        parser = argparse.ArgumentParser()
        parser.add_argument("url", type=str, nargs="?", help="URL")
        parser.add_argument("--version", action="version", version="Version 1.3", help="Prints version info")
        parser.add_argument("--json", action="store_true", help="Prints result as JSON in stdout")
        parser.add_argument("--verbose", action="store_true", help="Outputs verbose status messages")
        parser.add_argument("--limit", dest="limit", default=sys.maxsize, type=int,
                            help="Limit news topics if this parameter provided")
        parser.add_argument("--date", action="store", type=__date__, help="Find news in cache by date")
        self.args = parser.parse_args()

    def __get_info__(self, logger: logging):  # receive information from the site and return info_list
        info_list = list()
        response = requests.get(self.args.url)
        root = ELTree.fromstring(requests.utils.get_unicode_from_response(response))
        feed = None
        for item in root[0]:
            if item.tag == "title":
                feed = item.text
            if item.tag == "item":  # limit the number of news
                info_dict = dict()  # create a dictionary and fill it with news
                info_dict.update({"Feed": feed})
                for child in item:
                    if child.tag == "title":
                        info_dict.update({"Title": child.text})
                    elif child.tag == "pubDate":
                        try:
                            date = datetime.datetime.strptime(child.text, "%Y-%m-%dT%H:%M:%SZ")
                            info_dict.update(
                                {"Date": date.strftime("%a, %d %b %Y %H:%M:%S")})
                        except ValueError:
                            logger.warning("Date format error") if self.args.verbose else print("Date format error")
                    elif child.tag == "link":
                        info_dict.update({"Link": child.text})
                    # elif "content" in child.tag:  # can be used if necessary
                    #     info_dict.update({"Media": child.attrib["url"]})
                    elif child.tag == "source":
                        info_dict.update({"Source": child.text})
                        info_dict.update({"Source URL": child.attrib["url"]})
                info_list.append(info_dict)
        logger.info("The RSS news is read successfully")
        self.__cache_news__(info_list)
        return info_list[:self.args.limit]

    def __print_info__(self, logger: logging):  # the method outputs the information in the specific format
        if self.args.date is not None:
            info_list = self.__find_in_cache__()
        else:
            info_list = self.__get_info__(logger)  # get a list of news from __get_info__ method
        if self.args.json:  # output the news to a json file
            # get the root folder to write a json file there
            root = self.root + "\\news.json"
            try:
                file = open(root, "w", encoding='utf8')
                logger.info("File is open")
                json.dump(info_list, file, ensure_ascii=False)
                file.close()
                logger.info("The file was successfully written") if self.args.verbose else print(
                    "The file was successfully written")
            except OSError:
                logger.error("File write error") if self.args.verbose else print("File write error")
        elif not self.args.json:  # output the news to the console
            for item in info_list:
                print("")
                for key in item.keys():
                    print(key + ": " + item[key])
                print("")

    def __cache_news__(self, info_list: list()):
        root = self.root + "\\cache.json"
        data = list()
        if os.path.getsize(root) > 0:
            with open(root, "r", encoding='utf-8') as f:
                data = json.load(f)
        for item in info_list:
            if item.get("Link") not in data:
                if len(data) >= 1000:
                    data.pop(0)
                data.append(item)
        with open(root, "w", encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)

    def __find_in_cache__(self):
        find_in_cache = list()
        root = self.root + "\\cache.json"
        with open(root, "r", encoding='utf-8') as f:
            data = json.load(f)
        for item in data:
            if self.args.date == datetime.datetime.strptime(item.get("Date"), "%a, %d %b %Y %H:%M:%S").strftime(
                    "%Y%m%d"):
                find_in_cache.append(item)
        return find_in_cache[:self.args.limit]
